import chess
import cv2
import os
from analysis_move.main import main as analysis_move
from extract_video.main import extract_unique_frames
from chesscog.recognition.recognition import ChessRecognizer
from recap import URI

recognizer = ChessRecognizer(URI("models://"))

def predict_state(frame, idx):
    print('predicting frame', idx+1)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    board, *_ = recognizer.predict(img, chess.BLACK)
    return board.board_fen()

def extract_moves(video_path):
    frames = extract_unique_frames(video_path, frame_rate=1, threshold=0.95)
    fens = [predict_state(frame, idx) for idx, frame in enumerate(frames)]
    for idx, fen in enumerate(fens):
        print( f"Frame {idx+1}: https://lichess.org/editor/{fen}")
    moves = analysis_move(fens)
    print('moves', moves)
    return moves


if __name__ == "__main__":
    # read video path from args
    # import argparse
    # parser = argparse.ArgumentParser(description="Extract unique frames from a video.")
    # parser.add_argument("video_path", type=str, help="Path to the input video file.")
    # args = parser.parse_args()

    # video_path = args.video_path
    root = "C:/Users/Athens/Downloads/cu-chess-detection/test_videos"
    
    res = [['row_id', "output"]]
    for filename in os.listdir(root):
        video_path = os.path.join(root, filename)
        moves = extract_moves(video_path)
        res.append([filename, moves])
        
    # write to csv
    import csv
    with open('C:/Users/Athens/Downloads/output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(res)
    
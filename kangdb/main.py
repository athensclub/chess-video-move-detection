import chess
import cv2
from analysis_move.main import analysis_move
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
    print('moves',analysis_move(fens))


if __name__ == "__main__":
    # read video path from args
    import argparse
    parser = argparse.ArgumentParser(description="Extract unique frames from a video.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    args = parser.parse_args()

    video_path = args.video_path
    extract_moves(video_path)
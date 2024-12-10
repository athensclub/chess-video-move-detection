import cv2
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim

def extract_unique_frames(video_path, frame_rate=3, threshold=0.97):
    """
    Extract one frame per second from a video, keeping only frames that differ significantly from the previous frame.

    Parameters:
        video_path (str): Path to the input video file.
        frame_rate (int): Number of frames to process per second.
        threshold (float): Similarity threshold for frame comparison (0.0 to 1.0).
    
    Returns:
        list: List of unique frames (as numpy arrays).
    """
    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return []

    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"Video Info - FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.2f} seconds")

    # Initialize variables
    frame_count = 0
    frame_interval = fps * frame_rate
    unique_frames = []  # List to hold the unique frames
    prev_frame = None

    while True:
        ret, frame = video.read()
        if not ret:
            break  # Break the loop if no more frames are available

        # Process only 1 frame per second
        if frame_count % frame_interval == 0:
            # Convert frame to grayscale for comparison
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Compare with the previous frame
            if prev_frame is not None:
                score, _ = ssim(gray_frame, prev_frame, full=True)
                if score >= threshold:
                    # Frames are too similar, skip saving
                    frame_count += 1
                    continue
                
            
            # Append the frame to the list of unique frames
            unique_frames.append(frame)
            print(f"Stored frame {len(unique_frames)} at {frame_count / fps:.2f} seconds")

            output_file = os.path.join("C:/Users/Athens/Downloads/frames", f"frame_{len(unique_frames):04d}.png")
            cv2.imwrite(output_file, frame)
            
            # Update the previous frame
            prev_frame = gray_frame

        frame_count += 1

    video.release()
    print("Unique frame extraction completed!")
    return unique_frames


def main(video_path, frame_rate=1, threshold=0.65):
    # Usage
    video_path = "test1.mp4"  # Replace with your video file path
    unique_frames = extract_unique_frames(video_path, frame_rate, threshold)

    # Example: Accessing the stored frames
    print(f"Total unique frames: {len(unique_frames)}")

    # Assuming `unique_frames` contains the frames from the previous extraction
    # if unique_frames:
    #     display_frames_colab(unique_frames, delay=1000)  # 1000 ms (1 second) delay per frame
    # else:
    #     print("No unique frames to display.")

    return unique_frames

if __name__ == "__main__":
    # read video path from args
    import argparse
    parser = argparse.ArgumentParser(description="Extract unique frames from a video.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    args = parser.parse_args()

    video_path = args.video_path
    unique_frames = main(video_path)
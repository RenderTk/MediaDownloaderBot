import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up to the root directory
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
VIDEO_PATH = os.path.join(root_dir, "media", "video")
AUDIO_PATH = os.path.join(root_dir, "media", "audio")
OUTPUT_PATH = os.path.join(root_dir, "media", "output")

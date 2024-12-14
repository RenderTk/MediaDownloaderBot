import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate up to the root directory
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
VIDEO_PATH = os.path.join(root_dir, "media", "video")
AUDIO_PATH = os.path.join(root_dir, "media", "audio")
OUTPUT_PATH = os.path.join(root_dir, "media", "output")

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_SESSION_DIR_PATH = os.getenv("INSTAGRAM_SESSION_DIR_PATH")
INSTAGRAM_SESSION_FILEPATH = os.path.join(
    INSTAGRAM_SESSION_DIR_PATH, INSTAGRAM_USERNAME
)
TIK_TOK_MS_TOKEN = os.getenv("TIK_TOK_MS_TOKEN")

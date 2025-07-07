import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
OUTPUT_PATH = os.path.join(root_dir, "media")

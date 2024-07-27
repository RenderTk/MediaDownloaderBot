import sys
import os


_current_dir = os.path.dirname(os.path.abspath(__file__))
function_txt_filepath = os.path.join(_current_dir, "tik_tok_function.txt")


# "D:\My Files\Dev\MediaDownloaderBot\.venv\Lib\site-packages\pyktok\pyktok.py"
def get_pyktok_path():
    # Get the path to the root of the virtual environment
    virtual_env_root = sys.prefix

    # Construct the path to pyktok.py within the virtual environment
    pyktok_path = os.path.join(
        virtual_env_root, "Lib", "site-packages", "pyktok", "pyktok.py"
    )

    return pyktok_path


def import_function():
    fucntion_as_text = ""
    with open(function_txt_filepath, "r") as file:
        fucntion_as_text = file.read()

    # Append the content to the destination file
    with open(get_pyktok_path(), "a") as destination_file:
        destination_file.write("\n")  # Optional: add a newline before appending
        destination_file.write("\n")  # Optional: add a newline before appending
        destination_file.write(fucntion_as_text)


import_function()

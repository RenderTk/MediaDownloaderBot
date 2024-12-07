import sys
import os


_current_dir = os.path.dirname(os.path.abspath(__file__))
function_txt_filepath = os.path.join(_current_dir, "tik_tok_function.txt")


def get_pyktok_path():
    # Get the path to the root of the virtual environment
    virtual_env_root = sys.prefix
    if not os.path.isdir(virtual_env_root):
        raise FileNotFoundError("Virtual enviorment is not created yet.")
    # Construct the path to pyktok.py within the virtual environment
    pyktok_path = os.path.join(
        virtual_env_root, "lib", "python3.12", "site-packages", "pyktok", "pyktok.py"
    )

    return pyktok_path


def import_function(function_txt_filepath, pyktok_path):
    try:
        # Read the content of the source file
        with open(function_txt_filepath, "r") as file:
            function_as_text = file.read()

        # Get the path to the destination file
        destination_path = pyktok_path

        # Read the existing content of the destination file
        try:
            with open(destination_path, "r") as destination_file:
                existing_content = destination_file.read()
        except FileNotFoundError:
            existing_content = ""

        # Check if the function is already present
        if function_as_text in existing_content:
            print("Function is already present in the destination file.")
        else:
            # Append the content to the destination file
            with open(destination_path, "a") as destination_file:
                # Optionally add newlines for separation
                destination_file.write("\n")
                destination_file.write(function_as_text)

            print(
                f"Function successfully imported from '{function_txt_filepath}' to '{destination_path}'."
            )

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"IO Error: {e}")


import_function(function_txt_filepath, get_pyktok_path())

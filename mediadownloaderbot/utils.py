import string
import unicodedata
import subprocess
import os

_current_dir = os.path.dirname(os.path.abspath(__file__))

video_path = os.path.join(_current_dir, "media", "yt", "video")
audio_path = os.path.join(_current_dir, "media", "yt", "audio")
output_path = os.path.join(_current_dir, "media", "yt", "output")


def encode_to_base64(url):
    import base64

    encoded_bytes = base64.urlsafe_b64encode(url.encode())
    return encoded_bytes.decode()


def decode_from_base64(encoded_url):
    import base64

    decoded_bytes = base64.urlsafe_b64decode(encoded_url.encode())
    return decoded_bytes.decode()


def make_safe_filename(filename, replacement="_"):
    """
    Make a filename safe for saving in file explorer.

    Args:
    - filename (str): The original filename.
    - replacement (str): Optional. The character to replace unsafe characters with.
                         Defaults to underscore '_'.

    Returns:
    - str: A safe filename.
    """
    # Characters considered safe in most file systems
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

    # Remove any character not in the valid list
    cleaned_filename = (
        unicodedata.normalize("NFKD", filename).encode("ASCII", "ignore").decode()
    )
    safe_filename = "".join(
        c if c in valid_chars else replacement for c in cleaned_filename
    )

    # Remove leading/trailing spaces and replace sequences of spaces with a single space
    safe_filename = safe_filename.strip().replace(" ", replacement)

    return safe_filename


def merge_video_and_audio_from_files(
    video_path: str, audio_path: str, output_path: str
):
    # Comando ffmpeg
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-i",
        audio_path,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        output_path,
    ]
    # Ejecuta el comando
    subprocess.run(command, check=True)
    os.remove(video_path)
    os.remove(audio_path)

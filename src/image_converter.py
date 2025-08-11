from PIL import Image
from extension_manager import extensionDetector

def image_converter(input_path, output_path):
    """
    Opens an image from `input_path` and saves it as the desired format to `output_path`. The function also asks for desired extension.
    """

    # Get the extension of the output file
    _, extension = extensionDetector(output_path)
    with Image.open(input_path) as img:
        img.save(
        output_path,
        format=extension,
        quality=100,        # max quality (minimal compression)
        subsampling=0,      # disable chroma subsampling
        optimize=True      # try to make file smaller without quality loss
      )

# TODO:
# 1. Update the function and let the user decide on the quality of the output file
# Eithter through slider or different options

from pydub import AudioSegment

def audio_converter(input_path, output_path):
    (
        AudioSegment
        .from_file(input_path)
        .export(
            output_path,
            format=output_path.rsplit('.', 1)[-1]  # infer format from file extension
        )
    )


# .ogg format has issues
# .wav


# example uses
# input_file = "/content/audio_samples/sample1.aac"
# output_file = "/content/sample1.mp3"
# audio_converter(input_file, output_file)
# audio_converter("recording.wav", "recording.flac")


# Add docstring
# ------------------------------
# Another version of audio converter - see if we should remove it or not
# from pydub import AudioSegment

# def audio_converter_pydub(input_path, output_path, output_format):
#     """
#     Converts an audio file from input_path to output_path using pydub.
#     """
#     try:
#         audio = AudioSegment.from_file(input_path)
#         audio.export(output_path, format=output_format)
#         print(f"Successfully converted {input_path} to {output_path}")
#     except Exception as e:
#         print(f"Error converting {input_path}: {e}")

# Example usage (you'll need to replace these with actual file paths)
# input_audio_file = "/content/Universal File Converter/Audio Samples/sample.wav" # Replace with your input audio file
# output_audio_file = "/content/Universal File Converter/Converted Files/Audio/sample_CONVERTED.mp3" # Replace with your desired output file
# output_format = "mp3" # Replace with your desired output format (e.g., "wav", "ogg")

# audio_converter_pydub(input_audio_file, output_audio_file, output_format)

# --------------------------
# To Play the audio sample
# from IPython.display import Audio, display

# # Embed and autoplay the audio in a notebook
# display(Audio(url="/content/audio_samples/sample1.m4a", autoplay=True))
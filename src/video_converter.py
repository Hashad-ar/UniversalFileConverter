import ffmpeg

def video_converter(input_path, output_path):

  (
      ffmpeg
      .input(input_path)
      .output(output_path, vcodec='copy', acodec='copy')  # Fastest, just remuxes streams
      .run()
  )

# Manage the error if the output file already exists, show a message


# Testing video_converter function
# input_file = "/content/Universal File Converter/Video Samples/SampleVideo_176x144_1mb.3gp"
# output_file = "/content/SampleVideo_176x144_1mb.mp4"

# video_converter(input_file, output_file)

# Video(output_file, embed=True, width=640)



# TODO
# Add quality option (overal bitrate and maybe framerate)
# check if the output file exists or not becasue it will fail the function
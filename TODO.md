# Image: PIL
# Audio: pydub
# Video: ffmpeg
# Document: `pdf2docx`, `docx`, `python-docx`, PyMuPDF

# -----------------------
# Completed Tasks:
# 2. search and find file converter package/s✅
# 3. begin by implementing the converter for images✅
# 4. Use the function and convert to desired format✅
# 5. Save the output file✅
# 1. Create Default Path for Converted files✅
# Ask the user weather they want to save the converted file to default path or desired path

# -----------------------

# TODO:
# 1. Test the program on all the available extenions - unittest
#   *. Strategy: Each input image should be converted to all the available suitable file formats
#   *. Put messages for successful or unsuccessful runs
#   *. Use Try and Exept to handle errors and avoid crashing the program
# Check if input path or file exists / output exists

# TODO:
# Test the pipeline to see if it works well with audio files
# Test it for all the sample audio files
# do the document conversion part
# do unittests
# The pdf2docx library worked fine but it failed to convert diagrams (not images) to document

# TODO:
# Find all the compatible conversions between pairs in documents
# Based on the input file extension (for doc), show only the allowable dest. extensions
# FUTURE: In GUI, disable incompatible conversions (gray out the disabled items)
# any doc format to pdf or any other doc format, unoconv is the way to go
# but for pdf to other formats, pdf2docx is preffered
# Put the doc_converter function to main pipeline, test it and finish the main pipeline
# Check for other possible conversions of documents to see if we can support


# TODO - 7/7/2025
# Add support for conversion markdown to other formats
# ** for doc conversion from pdf to other formats, since only pdf to docx is supported, we can bypass it by first
# converting pdf to docx then convert docx to desired output format

# Create temporary folder to store temp files (like temp. files to do the conversion from pdf to docx and docx to odt)
# temporary folders for each file type like images, videos, documents, audio

# Clean up the project folder
# put each converter function into its own python file and then import them in main code
import subprocess
from pdf2docx import Converter


# General doc converter - from any format (not pdf) to any format (including pdf)
def doc_converter_main(input_path, output_path):
    # Input formats: .doc, .docx, .odt, .rtf, .txt, .ppt, .pptx, .xls, .xlsx, and many more.
    # Output formats: .pdf, .doc, .docx, .odt, .rtf, .txt, .ppt, .pptx, .xls, .xlsx, and more.
    subprocess.run([
        "unoconv", "-f", output_path.split('.')[-1], "-o", output_path, input_path
    ], check=True)

# doc → pdf

# ---------------------------
# Specifically for pdf to word document

def pdf2docx(src, dst):
    """
    Converts a PDF file to DOCX using the pdf2docx library.

    Args:
        src (str): The path to the input PDF file.
        dst (str): The path for the output DOCX file.
    """
    try:
        cv = Converter(src)
        cv.convert(dst)  # default pages="all"
        cv.close()
        print(f"Successfully converted {src} to {dst}")
    except Exception as e:
        print(f"Error converting {src} to {dst}: {e}")

# Example usage:
# input_pdf_file = "/content/Universal File Converter/Doc Samples/file-sample_150kB.pdf"  # Replace with your input PDF file
# output_docx_file = "/content/Universal File Converter/Converted Files/Documents/file-sample_150kB_CONVERTED.docx" # Replace with your desired output DOCX file

# pdf2docx(input_pdf_file, output_docx_file)

# ---------------------------

def doc_converter(input_path, output_path, inputFileExtension, selectedFormat):
  if inputFileExtension != "pdf":
    doc_converter_main(input_path, output_path)
    print(f"Successfully converted {input_path} to {output_path}")
  else:
    if selectedFormat == "docx":
      pdf2docx(input_path, output_path)
    else:
      print("Conversion is not supported at the moment")

# Example Usecase
# doc_converter(input_path, output_path)
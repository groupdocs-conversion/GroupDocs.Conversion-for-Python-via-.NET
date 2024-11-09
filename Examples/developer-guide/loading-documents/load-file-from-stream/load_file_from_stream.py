import os
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def get_file_stream(file_path: str):
    file_stream = open(file_path, "rb")
    return file_stream

def get_load_options(file_path: str):
    file_extension = os.path.splitext(file_path)[1]   
    possible_conversions = Converter.get_possible_conversions_by_extension(file_extension)
    load_options = possible_conversions.load_options
    return load_options

def load_file_from_stream():
    # Set file path
    file_path = "./annual-review.docx"

    # Retrieve file stream and load options
    file_stream = get_file_stream(file_path)
    load_options = get_load_options(file_path)

    # Specify source file stream and load options
    converter = Converter(file_stream, load_options)
    
    # Specify output file location and convert options
    output_path = "./annual-review.pdf"
    pdf_options = PdfConvertOptions()
    
    # Convert and save to output path
    converter.convert(output_path, pdf_options)

if __name__ == "__main__":
    load_file_from_stream()

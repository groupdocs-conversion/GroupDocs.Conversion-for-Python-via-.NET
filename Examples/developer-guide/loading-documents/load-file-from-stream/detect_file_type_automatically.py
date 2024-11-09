from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def get_file_stream(file_path: str):
    file_stream = open(file_path, "rb")
    return file_stream

def detect_file_type_automatically():
    # Retrieve file stream
    file_path = "./annual-review.docx"
    file_stream = get_file_stream(file_path)

    # Specify source file location
    converter = Converter(file_stream)
    
    # Specify output file location and convert options
    output_path = "./annual-review.pdf"
    pdf_options = PdfConvertOptions()
    
    # Convert and save to output path
    converter.convert(output_path, pdf_options)

if __name__ == "__main__":
    detect_file_type_automatically()

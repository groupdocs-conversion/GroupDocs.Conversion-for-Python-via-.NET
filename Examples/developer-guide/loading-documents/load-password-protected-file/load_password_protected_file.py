from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions
from groupdocs.conversion.options.load import WordProcessingLoadOptions

def load_password_protected_file():
    # Set file path
    file_path = "./password-protected.docx"
    
    # Instantiate load options and set password
    wp_load_options = WordProcessingLoadOptions()
    wp_load_options.password = "12345"

    # Specify source file stream and load options
    converter = Converter(file_path, wp_load_options)
    
    # Specify output file location and convert options
    output_path = "./password-protected.pdf"
    pdf_convert_options = PdfConvertOptions()
    pdf_convert_options.password = "67890"

    # Convert and save to output path
    converter.convert(output_path, pdf_convert_options)

if __name__ == "__main__":
    load_password_protected_file()

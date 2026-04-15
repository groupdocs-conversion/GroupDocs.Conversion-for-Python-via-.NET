from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_files_within_document_container():
    # Instantiate Converter with the input document container
    with Converter("./compressed.zip") as converter:
        # Instantiate convert options
        pdf_convert_options = PdfConvertOptions()

        # Extract the archive, convert the contained files, and save a consolidated PDF
        converter.convert("./converted.pdf", pdf_convert_options)

if __name__ == "__main__":
    convert_files_within_document_container()
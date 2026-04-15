from groupdocs.conversion import Converter
from groupdocs.conversion.filetypes import ImageFileType
from groupdocs.conversion.options.convert import ImageConvertOptions

def convert_specific_document_page_to_file():
    # Instantiate Converter with the input document
    with Converter("./basic-presentation.pptx") as converter:
        # Instantiate convert options
        png_convert_options = ImageConvertOptions()
        # Define the output format as PNG
        png_convert_options.format = ImageFileType.PNG

        # Specify the single page to convert
        png_convert_options.page_number = 3
        png_convert_options.pages_count = 1

        # Save the converted page to a file
        converter.convert("./slide-3.png", png_convert_options)

if __name__ == "__main__":
    convert_specific_document_page_to_file()
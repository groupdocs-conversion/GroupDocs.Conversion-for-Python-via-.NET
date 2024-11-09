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
        
        # Set the page number to convert and save it to a file
        page_number_to_convert = 5
        with open(f"./slide-{page_number_to_convert}.png", "w+b") as page_stream:
            converter.convert_by_page(page_stream, page_number_to_convert, png_convert_options)    

if __name__ == "__main__":
    convert_specific_document_page_to_file()

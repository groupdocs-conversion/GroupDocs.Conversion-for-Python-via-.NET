from groupdocs.conversion import Converter
from groupdocs.conversion.filetypes import ImageFileType
from groupdocs.conversion.options.convert import ImageConvertOptions

def convert_all_document_pages():
    # Instantiate Converter with the input document 
    with Converter("./basic-presentation.pptx") as converter:
        # Instantiate convert options 
        png_convert_options = ImageConvertOptions()
        # Define the output format as PNG
        png_convert_options.format = ImageFileType.PNG
        
        # Convert all pages and save to the output folder
        converter.convert_by_page("./converted-pages", png_convert_options)    

if __name__ == "__main__":
    convert_all_document_pages()

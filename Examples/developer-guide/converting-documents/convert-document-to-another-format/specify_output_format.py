from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import WordProcessingConvertOptions
from groupdocs.conversion.filetypes import WordProcessingFileType

def specify_output_format():
    # Instantiate Converter with the input document 
    with Converter("./business-plan.docx") as converter:
        # Instantiate convert options to define the output format
        word_convert_options = WordProcessingConvertOptions()
        # Set the output fomormat to TXT
        word_convert_options.format = WordProcessingFileType.TXT
        
        # Convert the input document to TXT
        converter.convert("./business-plan.txt", word_convert_options)    

if __name__ == "__main__":
    specify_output_format()
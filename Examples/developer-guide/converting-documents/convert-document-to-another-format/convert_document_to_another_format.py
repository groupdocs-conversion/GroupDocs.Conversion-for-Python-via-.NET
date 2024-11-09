from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_document_to_another_format():
    # Instantiate Converter with the input document 
    with Converter("./business-plan.docx") as converter:
        # Instantiate convert options to define the output format
        pdf_convert_options = PdfConvertOptions()
        
        # Convert the input document to PDF
        converter.convert("./business-plan.pdf", pdf_convert_options)    

if __name__ == "__main__":
    convert_document_to_another_format()

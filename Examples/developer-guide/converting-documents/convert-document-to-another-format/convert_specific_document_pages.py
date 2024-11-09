from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_specific_document_pages():
    # Instantiate Converter with the input document 
    with Converter("./business-plan.docx") as converter:
        # Instantiate convert options to define the output format
        pdf_convert_options = PdfConvertOptions()
        # Specify which document pages to convert
        pdf_convert_options.pages = [1, 3, 5]

        # Convert the specified pages of the input document to PDF
        converter.convert("./pages-1-3-5.pdf", pdf_convert_options)    

if __name__ == "__main__":
    convert_specific_document_pages()

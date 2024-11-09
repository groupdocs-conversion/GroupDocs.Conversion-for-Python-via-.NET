from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_consecutive_document_pages():
    # Instantiate Converter with the input document 
    with Converter("./business-plan.docx") as converter:
        # Instantiate convert options to define the output format
        pdf_convert_options = PdfConvertOptions()
        # Specify the starting page and number of pages to convert
        pdf_convert_options.page_number = 1
        pdf_convert_options.pages_count = 5

        # Convert the specified range of pages in the document to PDF
        converter.convert("./pages-1-through-5.pdf", pdf_convert_options)    

if __name__ == "__main__":
    convert_consecutive_document_pages()

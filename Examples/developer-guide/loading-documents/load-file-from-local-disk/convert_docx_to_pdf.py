from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_docx_to_pdf():
    # Specify source file location
    converter = Converter("./business-plan.docx")
    
    # Specify output file location and convert options
    output_path = "./business-plan.pdf"
    pdf_options = PdfConvertOptions()
    
    # Convert and save to output path
    converter.convert(output_path, pdf_options)

if __name__ == "__main__":
    convert_docx_to_pdf()

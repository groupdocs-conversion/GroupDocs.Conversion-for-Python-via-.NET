import os
from groupdocs.conversion import License, Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_docx_to_pdf():
    # Get license file absolute path
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    if license_path:
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load DOCX file
    with Converter("business-plan.docx") as converter:
        # Create convert options
        pdf_convert_options = PdfConvertOptions()

        # Convert DOCX to PDF
        converter.convert("./business-plan.pdf", pdf_convert_options)    

if __name__ == "__main__":
    convert_docx_to_pdf()

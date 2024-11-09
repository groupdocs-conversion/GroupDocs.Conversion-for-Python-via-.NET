import os
from groupdocs.conversion import License, Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def convert_files_in_archive():
    # Get license file absolute path
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    if license_path:
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load ZIP file
    with Converter("compressed.zip") as converter:
        # Create convert options
        pdf_convert_options = PdfConvertOptions()
        
        # Extract ZIP and convert each file to PDF
        converter.convert_multiple("./converted-files", pdf_convert_options)    

if __name__ == "__main__":
    convert_files_in_archive()

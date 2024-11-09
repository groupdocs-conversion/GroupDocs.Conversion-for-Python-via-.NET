import os
from groupdocs.conversion import License, Converter
from groupdocs.conversion.filetypes import ImageFileType
from groupdocs.conversion.options.convert import ImageConvertOptions

def convert_pdf_pages_to_png():
    # Get license file absolute path
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    if license_path:
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load PDF document
    with Converter("annual-review.pdf") as converter:
        # Create convert options
        png_convert_options = ImageConvertOptions()
        png_convert_options.format = ImageFileType.PNG
        
        # Convert document pages and save converted pages in the output folder
        converter.convert_by_page("converted-pages", png_convert_options)    

if __name__ == "__main__":
    convert_pdf_pages_to_png()

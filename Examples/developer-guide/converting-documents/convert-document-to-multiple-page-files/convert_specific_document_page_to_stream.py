import io
from groupdocs.conversion import Converter
from groupdocs.conversion.filetypes import ImageFileType
from groupdocs.conversion.options.convert import ImageConvertOptions

def convert_specific_document_page_to_stream():
    page_number_to_convert = 5
    output_file = f"./slide-{page_number_to_convert}.png"

    # Instantiate Converter with the input document
    with Converter("./basic-presentation.pptx") as converter:
        # Instantiate convert options
        png_convert_options = ImageConvertOptions()
        # Define the output format as PNG
        png_convert_options.format = ImageFileType.PNG

        # Specify the single page to convert
        png_convert_options.page_number = page_number_to_convert
        png_convert_options.pages_count = 1

        # Convert and save the page to a file on disk
        converter.convert(output_file, png_convert_options)

    # Load the converted page into an in-memory stream for downstream use
    with open(output_file, "rb") as file_handle:
        page_stream = io.BytesIO(file_handle.read())

    # page_stream now holds the PNG bytes and can be passed to any consumer
    print(f"Loaded {page_stream.getbuffer().nbytes} bytes into memory")

if __name__ == "__main__":
    convert_specific_document_page_to_stream()
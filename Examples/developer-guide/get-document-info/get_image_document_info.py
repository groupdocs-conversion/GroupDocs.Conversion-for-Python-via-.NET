from groupdocs.conversion import Converter

def get_image_document_info():
    # Load the document and retrieve information
    with Converter("./infographic-elements.tiff") as converter:
        doc_info = converter.get_document_info()

        # Print TIFF document info
        print("Bits per Pixel:", doc_info.bits_per_pixel)
        print("Creation Date:", doc_info.creation_date)
        print("Format:", doc_info.format)
        print("Height:", doc_info.height)
        print("Width:", doc_info.width)
        print("Size, bytes:", doc_info.size)

if __name__ == "__main__":
    get_image_document_info()
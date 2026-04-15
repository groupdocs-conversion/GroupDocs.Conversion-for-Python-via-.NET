from groupdocs.conversion import Converter

def get_document_info():
    # Load the document and retrieve information
    with Converter("./lorem-ipsum.txt") as converter:
        info = converter.get_document_info()
    
        # Print basic document info
        print("Format:", info.format)
        print("Pages count:", info.pages_count)
        print("Creation date:", info.creation_date)
        print("Size, bytes:", info.size)

if __name__ == "__main__":
    get_document_info()
from groupdocs.conversion import Converter

def get_pres_document_info():
    # Load the document and retrieve information
    with Converter("./presentation-template.pptx") as converter:
        doc_info = converter.get_document_info()

        # Print PPTX document info
        print("Author:", doc_info.author)
        print("Creation Date:", doc_info.creation_date)
        print("Format:", doc_info.format)
        print("Is Password Protected:", doc_info.is_password_protected)
        print("Pages Count:", doc_info.pages_count)
        print("Size, bytes:", doc_info.size)
        print("Title:", doc_info.title)

if __name__ == "__main__":
    get_pres_document_info()
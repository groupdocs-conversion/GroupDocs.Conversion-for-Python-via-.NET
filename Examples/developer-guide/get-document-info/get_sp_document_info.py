from groupdocs.conversion import Converter

def get_sp_document_info():
    # Load the document and retrieve information
    with Converter("./cost-analysis.xlsx") as converter:
        doc_info = converter.get_document_info()

        # Print XLSX document info
        print("Author:", doc_info.author)
        print("Creation Date:", doc_info.creation_date)
        print("Format:", doc_info.format)
        print("Is Password Protected:", doc_info.is_password_protected)
        print("Pages Count:", doc_info.pages_count)
        print("Size, bytes:", doc_info.size)
        print("Title:", doc_info.title)
        print("Worksheets Count:", doc_info.worksheets_count)

if __name__ == "__main__":
    get_sp_document_info()
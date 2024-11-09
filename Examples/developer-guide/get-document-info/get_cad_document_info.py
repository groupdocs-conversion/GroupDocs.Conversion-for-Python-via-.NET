from groupdocs.conversion import Converter

def get_cad_document_info():
    # Load the document and retrieve information
    with Converter("./blocks-and-tables.dwg") as converter:
        doc_info = converter.get_document_info()

        # Print DWG document info
        print("Creation Date:", doc_info.creation_date)
        print("Format:", doc_info.format)
        print("Height:", doc_info.height)
        print("Width:", doc_info.width)
        print("Size, bytes:", doc_info.size)
        
        print("Layouts:")
        for layout in doc_info.layouts:
            print(" Layout:", layout)
        
        print("Layers:")
        for layer in doc_info.layers:
            print(" Layer:", layer)

if __name__ == "__main__":
    get_cad_document_info()

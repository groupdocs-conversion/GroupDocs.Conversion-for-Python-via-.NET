from groupdocs.conversion import Converter

def get_email_document_info():
    # Load the document and retrieve information
    with Converter("./invitation.eml") as converter:
        doc_info = converter.get_document_info()

        # Print EML document info
        print("Creation Date:", doc_info.creation_date)
        print("Format:", doc_info.format)
        print("Is Encrypted:", doc_info.is_encrypted)
        print("Is Body in HTML:", doc_info.is_html)
        print("Is Signed:", doc_info.is_signed)
        print("Size:", doc_info.size)
        print("Attachments Count:", doc_info.attachments_count)

        for attachment_name in doc_info.attachments_names:
            print("Attachment Name:", attachment_name)

if __name__ == "__main__":
    get_email_document_info()
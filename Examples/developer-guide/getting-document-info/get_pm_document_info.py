from groupdocs.conversion import Converter

def get_pm_document_info():
    # Load the document and retrieve information
    with Converter("./weekly-plan.mpp") as converter:
        doc_info = converter.get_document_info()

        # Print MPP document info
        print("Creation Date:", doc_info.creation_date)
        print("Start Date:", doc_info.start_date)
        print("End Date:", doc_info.end_date)
        print("Format:", doc_info.format)
        print("Size, bytes:", doc_info.size)
        print("Tasks Count:", doc_info.tasks_count)

if __name__ == "__main__":
    get_pm_document_info()
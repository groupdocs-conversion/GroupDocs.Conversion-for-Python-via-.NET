from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions

def quick_example():
    """Convert a DOCX document to PDF — the five-line hello-world."""
    with Converter("./business-plan.docx") as converter:
        options = PdfConvertOptions()
        converter.convert("./business-plan.pdf", options)

if __name__ == "__main__":
    quick_example()
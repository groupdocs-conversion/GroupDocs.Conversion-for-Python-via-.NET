import sys
from groupdocs.conversion import Converter, ConverterSettings
from groupdocs.conversion.logging import ConsoleLogger
from groupdocs.conversion.options.convert import PdfConvertOptions

def write_logs_to_file():
    log_file_path = "./log.txt"

    # Redirect standard output to a file so ConsoleLogger writes into it
    original_stdout = sys.stdout
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        sys.stdout = log_file
        try:
            # Create converter settings and attach the console logger
            converter_settings = ConverterSettings()
            converter_settings.logger = ConsoleLogger()

            # Load DOCX document and convert it to PDF
            with Converter("./business-plan.docx", converter_settings) as converter:
                pdf_convert_options = PdfConvertOptions()
                converter.convert("./business-plan.pdf", pdf_convert_options)
        finally:
            sys.stdout = original_stdout

if __name__ == "__main__":
    write_logs_to_file()
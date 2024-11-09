from groupdocs.conversion import Converter, ConverterSettings
from groupdocs.conversion.logging import ConsoleLogger
from groupdocs.conversion.options.convert import PdfConvertOptions

def write_logs_to_console():
    # Create a console logger
    console_logger = ConsoleLogger()

    # Create converter settings and pass logger 
    converter_settings = ConverterSettings()
    converter_settings.logger = console_logger

    # Load DOCX document and convert it to PDF
    with Converter("./business-plan.docx", converter_settings) as converter:
        pdf_convert_options = PdfConvertOptions()
        converter.convert("./business-plan.pdf", pdf_convert_options)    

if __name__ == "__main__":
    write_logs_to_console()

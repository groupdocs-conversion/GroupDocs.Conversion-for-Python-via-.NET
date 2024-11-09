from groupdocs.pydrawing import Color
from groupdocs.conversion import Converter
from groupdocs.conversion.options.convert import PdfConvertOptions, WatermarkTextOptions

def add_watermark_to_converted_document():
    # Instantiate Converter with the input document 
    with Converter("./professional-services.docx") as converter:
        # Set up the watermark options
        watermark = WatermarkTextOptions("DRAFT")
        watermark.color = Color.from_argb(128, 211, 211, 211) # lite gray
        watermark.top = 10
        watermark.left = 10
        watermark.width = 300
        watermark.height = 300
        watermark.background = True

        # Set up the conversion options
        options = PdfConvertOptions()
        options.watermark = watermark
        
        # Perform the conversion
        converter.convert("./professional-services.pdf", options)    

if __name__ == "__main__":
    add_watermark_to_converted_document()
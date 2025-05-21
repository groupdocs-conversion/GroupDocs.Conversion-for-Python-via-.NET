import os
import subprocess
import sys

# Set license path
os.environ["GROUPDOCS_LIC_PATH"] = "C://Licenses//GroupDocs.Total.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Conversion for Python via .NET Examples!
=================================================================

This script will run a series of examples showcasing
the features of GroupDocs.Conversion for Python via .NET. 
Each example demonstrates different use cases and document 
conversion functionalities such as:

- Extracting document information.
- Converting documents to various formats.
- Handling password-protected files.
- Working with file containers and archives.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API! 

=======================================================
"""
    print(intro_text)

examples = [
    # Getting Started
    "getting-started/quick-start-guide/convert_docx_to_pdf.py",
    "getting-started/quick-start-guide/convert_files_in_archive.py",
    "getting-started/quick-start-guide/convert_pdf_pages_to_png.py",

    # Loading Documents
    "developer-guide/loading-documents/get-default-load-options/get_default_load_options.py",
    "developer-guide/loading-documents/load-file-from-local-disk/convert_docx_to_pdf.py",
    "developer-guide/loading-documents/load-file-from-stream/detect_file_type_automatically.py",
    "developer-guide/loading-documents/load-file-from-stream/load_file_from_stream.py",
    "developer-guide/loading-documents/load-password-protected-file/load_password_protected_file.py",

    # Getting Document Information
    "developer-guide/get-document-info/get_cad_document_info.py",
    "developer-guide/get-document-info/get_document_info.py",
    "developer-guide/get-document-info/get_email_document_info.py",
    "developer-guide/get-document-info/get_image_document_info.py",
    "developer-guide/get-document-info/get_pdf_document_info.py",
    "developer-guide/get-document-info/get_pm_document_info.py",
    "developer-guide/get-document-info/get_pres_document_info.py",
    "developer-guide/get-document-info/get_sp_document_info.py",
    "developer-guide/get-document-info/get_wp_document_info.py",

    # Converting Documents
    # Get Possible Conversions
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions.py",
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions_by_file_extension.py",
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions_for_current_file.py",

    # Convert a Document to Another Format
    "developer-guide/converting-documents/convert-document-to-another-format/convert_document_to_another_format.py",
    "developer-guide/converting-documents/convert-document-to-another-format/specify_output_format.py",
    "developer-guide/converting-documents/convert-document-to-another-format/convert_consecutive_document_pages.py",
    "developer-guide/converting-documents/convert-document-to-another-format/convert_specific_document_pages.py",
 
    # Convert a Document to Multiple Page Files
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_all_document_pages.py",
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_specific_document_page_to_file.py",
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_specific_document_page_to_stream.py",
  
    # Convert Files Within Document Containers
    "developer-guide/converting-documents/convert-files-within-document-containers/convert_files_within_document_container.py",

    # Add a Watermark to Converted Document
    "developer-guide/converting-documents/add-watermark-to-converted-document/add_watermark_to_converted_document.py",
    
    # Logging and Diagnostics
    "developer-guide/logging-and-diagnostics/write_logs_to_console.py",
    "developer-guide/logging-and-diagnostics/write_logs_to_file.py",
    
    # Licensing
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
]

print_intro()

# Get current environment variables from the parent process
env = os.environ.copy()

# Run each example script
for example in examples:
    current_dir = os.path.dirname(__file__)
    example_path = os.path.join(current_dir, example)
    example_dir = os.path.dirname(example_path)

    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        # Execute the example script in the current environment
        subprocess.run(
            [sys.executable, example_path], 
            cwd=example_dir, 
            check=True, 
            env=env
        )
        print(f"{GREEN}Completed {example}{RESET}\n")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error running {example}: {e}{RESET}\n")


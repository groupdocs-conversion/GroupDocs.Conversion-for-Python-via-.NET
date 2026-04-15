import os
import sys
import traceback

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# converted Markdown that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Conversion.lic"

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

This script will run a series of examples showcasing how to convert documents between the formats supported by GroupDocs.Conversion.
Each example demonstrates different use cases and functionalities such as:

- Converting documents between 10,000+ format pairs.
- Selecting specific pages or page ranges to convert.
- Inspecting document metadata.
- Loading password-protected documents.
- Adding watermarks during conversion.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.conversion import License

    # First, check for license path in environment variable
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    # Set license if found
    if license_path and os.path.exists(license_path):
        license = License()
        license.set_license(license_path)
        print(f"{GREEN}License set from: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example by executing its script in-process."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)

    # Change to the example directory so relative paths work
    saved_cwd = os.getcwd()
    os.chdir(example_dir)
    try:
        code = open(full_path, "r", encoding="utf-8").read()
        exec(compile(code, full_path, "exec"), {"__name__": "__main__", "__file__": full_path})
    finally:
        os.chdir(saved_cwd)

examples = [
    "getting-started/quick-start-guide/convert_docx_to_pdf.py",
    "getting-started/quick-start-guide/convert_pdf_pages_to_png.py",
    "getting-started/quick-start-guide/convert_files_in_archive.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "developer-guide/loading-documents/get-default-load-options/get_default_load_options.py",
    "developer-guide/loading-documents/load-file-from-local-disk/convert_docx_to_pdf.py",
    "developer-guide/loading-documents/load-file-from-stream/load_file_from_stream.py",
    "developer-guide/loading-documents/load-file-from-stream/detect_file_type_automatically.py",
    "developer-guide/loading-documents/load-password-protected-file/load_password_protected_file.py",
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions.py",
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions_by_file_extension.py",
    "developer-guide/converting-documents/get-possible-conversions/get_all_possible_conversions_for_current_file.py",
    "developer-guide/converting-documents/convert-document-to-another-format/convert_document_to_another_format.py",
    "developer-guide/converting-documents/convert-document-to-another-format/specify_output_format.py",
    "developer-guide/converting-documents/convert-document-to-another-format/convert_specific_document_pages.py",
    "developer-guide/converting-documents/convert-document-to-another-format/convert_consecutive_document_pages.py",
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_all_document_pages.py",
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_specific_document_page_to_file.py",
    "developer-guide/converting-documents/convert-document-to-multiple-page-files/convert_specific_document_page_to_stream.py",
    "developer-guide/converting-documents/convert-files-within-document-containers/convert_files_within_document_container.py",
    "developer-guide/converting-documents/add-watermark-to-converted-document/add_watermark_to_converted_document.py",
    "developer-guide/getting-document-info/get_document_info.py",
    "developer-guide/getting-document-info/get_pdf_document_info.py",
    "developer-guide/getting-document-info/get_wp_document_info.py",
    "developer-guide/getting-document-info/get_pm_document_info.py",
    "developer-guide/getting-document-info/get_image_info.py",
    "developer-guide/getting-document-info/get_pres_document_info.py",
    "developer-guide/getting-document-info/get_sp_document_info.py",
    "developer-guide/getting-document-info/get_cad_document_info.py",
    "developer-guide/getting-document-info/get_email_document_info.py",
    "developer-guide/logging-and-diagnostics/write_logs_to_console.py",
    "developer-guide/logging-and-diagnostics/write_logs_to_file.py",
    "product-overview/quick_example.py",
]

print_intro()
set_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

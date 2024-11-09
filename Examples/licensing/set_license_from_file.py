import os
from groupdocs.conversion import License

def set_license_from_file():
    # Get absolution path to license file
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    if not license_path:
        print("Please obtain a license to run this example.")
        return

    # Instantiate License and set the license
    license = License()
    license.set_license(license_path)

if __name__ == "__main__":
    set_license_from_file()
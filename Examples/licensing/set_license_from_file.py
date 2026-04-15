import os
from groupdocs.conversion import License

def set_license_from_file():
    # Absolute path to the license file
    license_path = os.path.abspath("./GroupDocs.Conversion.PythonViaNET.lic")

    if not os.path.exists(license_path):
        print(f"License file not found: {license_path}")
        print("Place a valid .lic file at that path or set GROUPDOCS_LIC_PATH.")
        return

    # Instantiate License and apply the file
    license = License()
    license.set_license(license_path)
    print(f"License applied from: {license_path}")

if __name__ == "__main__":
    set_license_from_file()
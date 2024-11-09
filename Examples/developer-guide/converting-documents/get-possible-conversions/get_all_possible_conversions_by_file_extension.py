from groupdocs.conversion import Converter

def get_all_possible_conversions_by_file_extension():
    # Get all possible conversions
    possible_conversion = Converter.get_possible_conversions_by_extension("docx")

    # Filter primary conversions
    primary_conversions = [conversion.format for conversion in possible_conversion.all if conversion.is_primary]
    # Filter secondary conversions
    secondary_conversions = [conversion.format for conversion in possible_conversion.all if not conversion.is_primary]

    # Print out the source format and its conversions
    print(f" **Source format**: {possible_conversion.source.description}")
    print(f"  - **Primary conversions**: {primary_conversions}")
    print(f"  - **Secondary conversions**: {secondary_conversions}")
    print()

if __name__ == "__main__":
    get_all_possible_conversions_by_file_extension()

from groupdocs.conversion import Converter

def get_all_possible_conversions():
    # Get all possible conversions
    all_possible_conversions = Converter.get_all_possible_conversions()

    for possible_conversion in all_possible_conversions:
        # Filter primary conversions
        primary_conversions = [conversion.format for conversion in possible_conversion.all if conversion.is_primary]
        # Filter secondary conversions
        secondary_conversions = [conversion.format for conversion in possible_conversion.all if not conversion.is_primary]

        # Print out the source format and it's conversions
        print(f" **Source format**: {possible_conversion.source.description}")
        print(f"  - **Primary conversions**: {primary_conversions}")
        print(f"  - **Secondary conversions**: {secondary_conversions}")
        print()

if __name__ == "__main__":
    get_all_possible_conversions()
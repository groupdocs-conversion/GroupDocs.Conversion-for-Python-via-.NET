from groupdocs.conversion import Metered

PLACEHOLDER = "******"

def set_metered_license():
    # Set your public and private metered keys
    public_key = PLACEHOLDER
    private_key = PLACEHOLDER

    if public_key == PLACEHOLDER or private_key == PLACEHOLDER:
        print("Metered keys must be set before running this example.")
        print("Edit public_key and private_key with the credentials from")
        print("https://purchase.groupdocs.com/ to enable metered licensing.")
        return

    # Instantiate Metered and apply the keys
    metered = Metered()
    metered.set_metered_key(public_key, private_key)

    # Get number of MBs processed
    mb_processed = metered.get_consumption_quantity()
    print("MB processed:", mb_processed)

    # Get number of credits used
    credits_used = metered.get_consumption_credit()
    print("Credits used:", credits_used)

if __name__ == "__main__":
    set_metered_license()
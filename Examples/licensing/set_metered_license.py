from groupdocs.conversion import Metered

def set_metered_license():
    # Set your public and private keys
    public_key = "******" 
    private_key = "******" 

    if public_key == "******":
        print("Please obtain public and private keys to run this example.")
        return

    # Instantiate Metered and set keys
    metered = Metered()
    metered.set_metered_key(public_key, private_key)

    # Get a number of MBs processed 
    mb_processed = metered.get_consumption_quantity()
    print("MB processed: ", mb_processed)

    # Get a number of credits used
    credits_used = metered.get_consumption_credit()
    print("Credits used: ", credits_used)

if __name__ == "__main__":
    set_metered_license()
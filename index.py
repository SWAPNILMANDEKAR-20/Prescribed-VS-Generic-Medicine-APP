import requests

def get_generic_from_rxnorm(drug_name):
    """
    Fetches the generic equivalent of a prescribed drug using the RxNorm API.
    """
    # Base URLs
    rxnorm_base_url = "https://rxnav.nlm.nih.gov/REST"
    rxcui_url = f"{rxnorm_base_url}/rxcui.json?name={drug_name}"

    try:
        # Step 1: Get RxCUI for the given drug name
        rxcui_response = requests.get(rxcui_url)
        rxcui_response.raise_for_status()
        rxcui_data = rxcui_response.json()
        rxcui = rxcui_data.get("idGroup", {}).get("rxnormId", [None])[0]

        if not rxcui:
            print(f"No RxCUI found for '{drug_name}'. Check the drug name.")
            return

        # Step 2: Use RxCUI to find the generic equivalent
        generic_url = f"{rxnorm_base_url}/rxcui/{rxcui}/related.json?tty=IN"
        generic_response = requests.get(generic_url)
        generic_response.raise_for_status()
        generic_data = generic_response.json()

        # Extract generic names
        related_group = generic_data.get("relatedGroup", {})
        concept_properties = related_group.get("conceptGroup", [])
        generic_names = [
            prop.get("conceptProperties", [{}])[0].get("name", "Unknown")
            for group in concept_properties for prop in [group]
            if group.get("tty") == "IN"
        ]

        if generic_names:
            print(f"Generic names for '{drug_name}': {', '.join(generic_names)}")
        else:
            print(f"No generic equivalent found for '{drug_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to RxNorm API. {e}")

# Example usage
drug_name = input("Enter the prescribed drug name: ").strip()
get_generic_from_rxnorm(drug_name)



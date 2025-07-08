import requests

def get_drug_info(drug_name):
    api_url = "https://api.fda.gov/drug/label.json"
    
    # Search by brand name OR generic name
    params = {
        "search": f'openfda.brand_name:"{drug_name}" OR openfda.generic_name:"{drug_name}"',
        "limit": 5  # Retrieve up to 5 results
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        
        # Extract and display relevant drug information
        if "results" in data:
            for drug in data["results"]:
                brand_name = drug.get("openfda", {}).get("brand_name", ["N/A"])[0]
                generic_name = drug.get("openfda", {}).get("generic_name", ["N/A"])[0]
                manufacturer = drug.get("openfda", {}).get("manufacturer_name", ["N/A"])[0]
                purpose = drug.get("purpose", ["N/A"])[0]
                warnings = drug.get("warnings", ["N/A"])[0]

                print(f"\nBrand Name: {brand_name}")
                print(f"Generic Name: {generic_name}")
                print(f"Manufacturer: {manufacturer}")
                print(f"Purpose: {purpose}")
                print(f"Warnings: {warnings}")
        else:
            print("No results found for the given drug name.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
drug_name = input("Enter the drug name: ")
get_drug_info(drug_name)

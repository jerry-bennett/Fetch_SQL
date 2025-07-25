import json
import csv

def flatten_cpg(cpg):
    if isinstance(cpg, dict) and "$id" in cpg:
        return cpg["$id"]["$oid"]
    return None

def convert_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            headers = ["_id", "barcode", "category", "categoryCode", "cpg", "name", "topBrand"]
            writer.writerow(headers)
            
            # Write rows, flattening nested fields where needed
            for record in data:
                record["cpg"] = flatten_cpg(record.get("cpg"))
                writer.writerow([record.get(header) for header in headers])

# Example usage
convert_to_csv('brands_wrapped.json', 'brands.csv')

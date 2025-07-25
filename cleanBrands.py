import csv

def clean_brands_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the header
        headers = next(reader)
        writer.writerow(headers)
        
        for row in reader:
            # Clean the _id field (removing {'$oid': '...'})
            row[0] = row[0].strip("{}").split(":")[1].strip("'\" ")
            
            # Write the cleaned row to the output CSV
            writer.writerow(row)

# Example usage
clean_brands_csv('brands.csv', 'brands_cleaned.csv')

import json

def wrap_json_in_array(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    if not lines:
        print(f"Warning: {input_file} is empty, no data to wrap.")
        return

    # Add opening square bracket at the beginning
    lines = ['['] + [line.strip() for line in lines if line.strip()]  # Remove empty lines

    # Add closing square bracket at the end
    lines.append(']')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(lines):
            if i < len(lines) - 1:  # If it's not the last line
                outfile.write(line + ',\n')
            else:
                outfile.write(line + '\n')

# Usage example
#wrap_json_in_array('users.json', 'users_wrapped.json')
#wrap_json_in_array('receipts.json', 'receipts_wrapped.json')
wrap_json_in_array('brands.json', 'brands_wrapped.json')

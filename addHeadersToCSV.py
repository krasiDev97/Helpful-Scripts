
# THIS SCRIPT ADDS HEADERS TO THE NEW CSV FILES AFTER ANNOTATING, OR CAN CHANGE THE OLD HEADERS

import os

input_folder = ''
new_header = "Chromosome,Position,Reference,Alternative,Effect,Letter,Impact,Type,part of gene"  # your new header here

for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        filepath = os.path.join(input_folder, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Skip the first line (old header), keep the rest
        data_without_header = lines[1:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_header + '\n')
            f.writelines(data_without_header)

print("Old headers removed and new headers added.")

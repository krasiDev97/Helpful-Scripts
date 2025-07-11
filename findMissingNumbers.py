# IF YOUR SAMPLES ARE NAMED WITH CONSECUTIVE NUMBERS, YOU CAN USE THIS SCRIPT TO CHECK FOE MISSING FILES

import os

# input directory
directory = ""

# List all filenames in the folder
filenames = os.listdir(directory)

# extract numbers from filenames like .FASTQ or .FASTQ.gz
numbers = sorted([
    int(name.split('.')[0])
    for name in filenames
    if (name.endswith(".FASTQ") or name.endswith(".FASTQ.gz")) and name.split('.')[0].isdigit()
])

# detect gaps in sequence
missing = []
for i in range(numbers[0], numbers[-1]):
    if i not in numbers:
        missing.append(i)

# print result
if missing:
    print("Missing numbers in folder:")
    for num in missing:
        print(f"{num}.FASTQ")
else:
    print("No missing files in this folder.")

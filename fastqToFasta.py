import gzip
import os

# conversion
def fastq_2_fasta(fastq_gz_file, fasta_file):
    with gzip.open(fastq_gz_file, 'rt') as fq, open(fasta_file, 'w') as fa:
        while True:
            header = fq.readline().strip()
            if not header:
                break  # End of file
            sequence = fq.readline().strip()
            fq.readline()  # skip '+'
            fq.readline()  # skip quality

            fasta_header = ">" + header[1:]  # convert '@' to '>'
            fa.write(f"{fasta_header}\n{sequence}\n")


def batch_convert(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".FASTQ.gz"):
            fastq_path = os.path.join(input_folder, filename)
            fasta_filename = filename.replace(".FASTQ.gz", ".fasta")
            fasta_path = os.path.join(output_folder, fasta_filename)
            
            print(f"Converting: {filename} → {fasta_filename}")
            fastq_2_fasta(fastq_path, fasta_path)

# add input and output directories
input_dir = "/home/pc/Desktop/ADDED_FASTQ"
output_dir = "/home/pc/Desktop/ADDED_FASTQ/fasta"
batch_convert(input_dir, output_dir)

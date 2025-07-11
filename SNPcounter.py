# SCRIPT FOR COUNTING SNPs IN INDIVIDUAL SAMPLES, EXCLUDING INDELS AND MULTI-NUCLEOTIDE VARIANTS

import pysam
from collections import Counter

vcf_file = ""
vcf = pysam.VariantFile(vcf_file)

chrom_counts = Counter()
for rec in vcf.fetch():
    # check if variant is a SNP and chromosome name starts with "NC_" , NC are chromosomes named from NCBI assembly, that way it excludes NW scaffolds 
    if rec.chrom.startswith("NC_") and all(len(allele) == 1 for allele in [rec.ref] + list(rec.alts)):
        chrom_counts[rec.chrom] += 1

for chrom, count in chrom_counts.items():
    print(f"{chrom}: {count}")
    

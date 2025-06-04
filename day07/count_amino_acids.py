import sys
from textwrap import wrap

fasta_file = sys.argv[1]

with open(fasta_file, "r") as fh_read:
    fasta_list = fh_read.readlines()

fasta_sequence = ''.join(fasta_list[1:]) # takes all lines except first line and combines into 1 string
sequence_codons = wrap(fasta_sequence.replace("\n",""), 3) # breaks sequence into a list of 3-letter codon strings

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

by_codon = {} # this will store the reverse table, and map the codon to the amino acid

for amino_acid in codon_table: # amino_acid here is the name of each AA (i.e. it's a string)
    for i in range(len(codon_table[amino_acid])):
        by_codon[codon_table[amino_acid][i]] = amino_acid

aa_count = {}
for amino_acid in codon_table:
    aa_count[amino_acid] = 0 # initializing all count values of aa_count to be zero

for codon in sequence_codons:
    if len(codon) < 3:
        continue
    aa_count[by_codon[codon]] += 1

write_file = r'.\amino_acid_counted.txt'
with open(write_file, "w") as fh_write:
    for amino_acid in aa_count:
        fh_write.write(f"{amino_acid:<4} {aa_count[amino_acid]:>3}\n")


# Parse VCF for protein eliminating mutations

import re
def main():
    inputfile=open('vcf_otherstrand.vcf').read().split('\n')
    nodes=open('nonsense_mutations_COSMIC.txt').read().split('\n')

    for node in nodes:
        row = node.split('\t')
        for line in inputfile:
            if re.search(r'\b'+ row[1] + '\t'+ row[0] + r'\b', line):
               print(line)
main()

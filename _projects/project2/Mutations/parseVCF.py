# -------------------
# parseVCF.py parses the vcf file of mutations to include only those that are
# nonsense mutations according to COSMIC.
# -------------------


import re
def main():
    inputfile=open('231_SNV_correct.vcf').read().split('\n')
    nodes=open('nonsense_mutations_COSMIC.txt').read().split('\n')

    header = inputfile[:6]
    for line in header:
        print(line)
    for node in nodes:
        row = node.split('\t')
        for line in inputfile:
            if re.search(r'\b'+ row[1] + '\t'+ row[0] + r'\b', line):
               print(line)
main()

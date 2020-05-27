# Parse VCF for protein eliminating mutations

import re

def main():
    inputfile=open('231_SNV_COSMIC.vcf').read().split('\n')
##    nodes=open('nonsense_mutations_COSMIC.txt').read().split('\n')
    # the lists below come from the getRIGHTAA script, and tell you which VEP output they come from
    orig = ['AKAP2', 'CHD5_ENST00000262450', 'CLCN1', 'COL4A3', 'COL4A3_ENST00000328380', 'EPHA3', 'M6PR', 'MS4A3', 'MTBP', 'NF2', 'NF2_ENST00000403999', 'PALM2-AKAP2', 'PDGFRA', 'PON2', 'SKIV2L2', 'SLC11A1', 'TAB2', 'TCF25', 'TRIM41', 'TRIO', 'TTLL9', 'TTLL9_ENST00000375935']
    other = ['DENND1B', 'DENND1B_ENST00000367396', 'KLK9', 'NLRP11', 'PKDREJ', 'RHOBTB1', 'RPP40', 'TP53', 'TP53_ENST00000269305', 'TP53_ENST00000455263', 'UQCRC1', 'ZNF318']
             
    for node in orig:
        for line in inputfile:
            if re.search(r'\b'+ node + r'\b', line):
               print(line)
    for node in other:
        for line in inputfile:
            if re.search(r'\b' + node + r'\b', line):
                print(line)
main()

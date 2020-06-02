#----------------------
# switchVCF.py switches the bases in the vcf file to their complement to
# return the mutation on the other DNA strand.
#----------------------


import re
import statistics
def main():
    inputfile=open('231_SNV_COSMIC.vcf').read().split('\n')
    header = inputfile[:6] #save header
    inputfile = inputfile[6:] #remove first five lines

    for line in header:
        print(line)
    for lines in inputfile:
        line = lines.split('\t')
        if line[3] == 'A':
                line[3] = 'T'
        elif line[3] == 'T':
                line[3] = 'A'
        elif line[3] == 'C':
                line[3] = 'G'
        elif line[3] == 'G':
                line[3] = 'C'
        if line[4] == 'A':
                line[4] = 'T'
        elif line[4] == 'T':
                line[4] = 'A'
        elif line[4] == 'C':
                line[4] = 'G'
        elif line[4] == 'G':
                line[4] = 'C'
        print(line)   
main()

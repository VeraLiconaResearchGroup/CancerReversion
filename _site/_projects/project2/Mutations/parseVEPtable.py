# Parse VEP table for transcripts of interest

import re

def main():
    inputfile = open('231_otherstrand2.txt').read().split('\n')
    transcripts = open('transcripts_COSMIC.txt').read().split('\n')
    
    print(inputfile[0])
    for transcript in transcripts:
        for line in inputfile:
            if re.search(r'\b' + transcript +r'\b', line):
                print(line)

main()



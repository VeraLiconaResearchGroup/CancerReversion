import re

def main():
    inputfile = open('MOs Gene symbol_with complex.txt').read().split('\n')
    mo = ['MO000023615']
    LS = []

    for line in inputfile:
        row = line.split('\t')
        for id in mo:
            if re.search(r'\b' + id +r'\b', line):
                LS.append(row[0])
    print(LS, sep=':')

main()


import re
def main():
    data = open('IPAdata.txt').read().split('\n')
    FOC = open('FunDEGs_FOC_LCC_noHKG_80').read().split('\n')

    print(data[0])
    for line in data:
        row = line.split('\t')
        for node in FOC:
            if row[0] == node:
                print(line)
                

main()

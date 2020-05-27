import csv
import re
def main():
    MOfile=open('MOs Gene symbol.txt').read().split('\n')
    edgefile=open('edges.csv').read()
    outputfile=open('edges_geneSymbol.csv','w+')
    writer=csv.writer(outputfile, delimiter=',')

    MOs = []
    rep = []
    complex = {}
    
    for line in MOfile:
        text=line.split('\t')
        symbol=text[0]
        if ',' in text[1]:
            IDs=text[1].split(',')
            for MO in IDs:
                if MO in MOs:
                    rep.append(MO)
                MOs.append(MO)
        else:
            if text[1] in MOs:
                rep.append(text[1])
            MOs.append(text[1])

    for MO in rep:
        temp = []
        for line in MOfile:
            text=line.split('\t')
            if re.search(MO, text[1]):
               temp.append(text[0])
        comp = ':'.join(temp)
        complex[MO] = comp

    print("CHECK COMPLEXES:")
    i = 0
    for MO, comp in complex.items():
        print(MO, '\t', comp)
        i += 1
    print("number of complexes: ", i)
    
    ask = input("Do you want to change a complex? (y/n) " )
    while ask == "y":
        new = str(input("Input change in format: MO,new_symbol (no space): "))
        edit = new.split(',')
        complex[edit[0]] = edit[1]
        print(complex)
        ask = input("Do you want to change another complex? (y/n) " )

    for MO, comp in complex.items():
        edgefile = edgefile.replace(MO, comp)
           
    for line in MOfile:
        text=line.split('\t')
        symbol=text[0]
        if ',' in text[1]:
            IDs=text[1].split(',')
            for MO in IDs:
                edgefile=edgefile.replace(MO,text[0])
        else:
            edgefile=edgefile.replace(text[1],text[0])

    edgefile = edgefile.replace("MO000019230", "ubiquitin")

    outputfile.write(edgefile)
    outputfile.close()
main()
                

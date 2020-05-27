import csv
def main():
    inputfile=open('network_MOs Gene symbol.txt').read().split('\n')
    outputfile=open('IDs.csv','w+')
    writer=csv.writer(outputfile, delimiter=',')
    for line in inputfile:
        text=line.split('\t')
        symbol=text[0]
        print(text)
        if ',' in str(text[1]):
            IDs=str(text[1]).split(',')
            #TPsym=str(text[2]).split(',')
            i=0
            for i in range(len(IDs)):
                lines=[text[0],IDs[i]]
                print(lines)
                writer.writerow(lines)
                i=i+1
        else:
            lines=[text[0],text[1]]
            print(lines)
            writer.writerow(lines)
    outputfile.close()
main()
                

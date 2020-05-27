import csv
def main():
    MOfile=open('MOs Gene symbol_with complex.txt').read().split('\n')
    edgefile=open('edges.csv').read()
    outputfile=open('edges_GSID_complex.csv','w+')
    writer=csv.writer(outputfile, delimiter=',')
    for line in MOfile:
        text=line.split('\t')
        symbol=text[0]
        print(text)
        if ',' in text[1]:
            IDs=text[1].split(',')
            print(IDs)
            #TPsym=str(text[2]).split(',')
            i=0
            for i in range(len(IDs)):
                print(IDs[i])
                MO=IDs[i]
                lines=[text[0],IDs[i]]
                edgefile=edgefile.replace(MO,text[0])
                
                i=i+1
            
        else:
            lines=[text[0],text[1]]
            edgefile=edgefile.replace(text[1],text[0])
            
    outputfile.write(edgefile)
    outputfile.close()
main()
                

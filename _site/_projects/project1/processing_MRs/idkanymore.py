import re,csv

def main():
    inputfile=open('reduced.txt').read()
    ID_file=open('IDs.csv')
    IDs=csv.DictReader(ID_file)
    outputfile=open('cleanup.txt','w+')
    hello=inputfile
    for x in IDs:
        if len(x['Transpath ID'])>0:
            #hello=hello.replace(x['Transpath ID'],x['ID'])
            hello=re.sub(str(x['TP']),str(x['ID']),hello)
        #else:
            #hello=hello.replace(x['Transpath ID'],x['Transpath ID'])
    outputfile.write(hello)
    outputfile.close()
        
            
    
        
main()

import re
def main():
    file1=open('complete.fa').read().split('\n>')
   
    IDs=open('mutated_proteins Proteins Ensembl.txt').read().split('\n')
    
    outputfile=open('complete_genesymbol.fa','w+')
    for lines in IDs:
        line=lines.split('\t')
        PID=str(line[0])
        for line1 in file1:
            linesplit=line1.split('\n')
            ID=str(linesplit[0])
            dash=False
            colon=False
            if ':' in ID:
                IDsplit=ID.split(':')
                actualID=str(IDsplit[0])
                colon=True
            if '_' in ID:
                IDsplit=ID.split('_')
                actualID=str(IDsplit[0])
                dash=True
            if PID in actualID:
                if colon:
                    x='>'+str(line[3])+':'+str(IDsplit[1])
                if dash:
                    x='>'+str(line[3])+'_'+str(IDsplit[1])
                outstring=x+'\n'+str(linesplit[1])+'\n'
                outputfile.write(outstring)    
    outputfile.close()
    
main()
    
        
        
        
        

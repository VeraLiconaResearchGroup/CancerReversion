import re, csv

def main():
    inputfile=open('cleanup.txt').read().replace('-->',' -->').replace('{',' {').replace('{p}','')
    hi=re.sub(r'\([^)]*\)', '', inputfile).split('\n')
    outputfile=open('edges.csv', 'w+')
    writer=csv.writer(outputfile, delimiter=',')
    i=1
    for line in hi:
        if re.search(r'.-->',line):
            x=line.replace('  -->',' -->').split(' ')
            #print(x)
            arrowindex=x.index('-->')
            reactant=str(x[arrowindex-1]).replace('--','')
            product=str(x[arrowindex+1])
            edge=[reactant,product,'activates']
            print(str(i)+str(edge))
        if re.search(r'.--/',line):
            x=line.split(' ')
            #print(x)
            arrowindex=x.index('--/')
            reactant=str(x[arrowindex-1]).replace('--','')
            product=str(x[arrowindex+1])
            edge=[reactant,product,'inactivates']
            print(str(i)+str(edge))
        if re.search(r'<==>',line):
            x=line.split(' ')
            arrowindex=x.index('<==>')
            reactant=str(x[arrowindex-1]).replace('--','')
            product=str(x[arrowindex+1])
            edge=[reactant,product,'activates']
            print(str(i)+str(edge))
        writer.writerow(edge)
        i=i+1
    outputfile.close()
            
            
    
        
main()

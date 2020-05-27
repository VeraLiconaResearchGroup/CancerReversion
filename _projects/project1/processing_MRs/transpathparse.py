import re

def main():
    inputfile=open('network reactions').read().split("\n")
    outputfile=open('reduced.txt', 'w+')
    for line in inputfile:
        if re.search(r'.-->',line):
            outputfile.write(line)
            outputfile.write('\n')
        if re.search(r'.--/',line):
            outputfile.write(line)
            outputfile.write('\n')
    outputfile.close()
            
            
    
        
main()

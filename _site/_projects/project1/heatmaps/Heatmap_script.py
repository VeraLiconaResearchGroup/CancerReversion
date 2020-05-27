import re
import statistics
def main():
    inputfile=open('Heatmap_data.txt').read().split('\n')
    nodes=open('network_nodes.txt').read().split('\n')

## For average values:
##    for node in nodes:
##        for line in inputfile:
##            if re.search(r'\b'+ node + '\t'+r'\b', line):
##                lines = line.split('\t')
##                print(str(lines[0])+'\t'+str(lines[1])+'\t'+str(lines[2]))


## For each sample:
    for node in nodes:
        for line in inputfile:
            if re.search(r'\b'+ node + '\t'+r'\b', line):
                lines = line.split('\t')
                print(str(lines[0])+'\t'+str(lines[3])+'\t'+str(lines[4])+'\t'+str(lines[5])+'\t'+str(lines[6])+'\t'+str(lines[7])+'\t'+str(lines[8])+'\t'+str(lines[9])+'\t'+str(lines[10]))
main()

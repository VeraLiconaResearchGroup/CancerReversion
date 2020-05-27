
def main():
    inputfile = open('attractor_10A.txt').read().split('\n')
    BDO = open('rons_8').read().split('\n')

    for node in inputfile:
        if node in BDO:
            print(node)

    
main()

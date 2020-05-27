import re
def main():
    file = open("attractor_231.txt").read().split('\n')
    nodes = open("rons_8").read().split('\n')

    for node in nodes:
        for line in file:
            row = line.split(' ')
            if row[0] == node:
                print(row[1])

main()

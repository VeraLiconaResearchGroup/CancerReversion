# Discretize data

def main():
    file = open("attractor_10A.txt").read().split('\n')

    for line in file:
        row = line.split(' ')
        for i in range(len(row)):
            if i > 0:
                row[i] = float(row[i])
                if row[i] > 0:
                    row[i] = 1
                elif row[i] == 0:
                    row[i] = 0
                elif row[i] <0:
                    row[i] = -1
        print(row)

main()

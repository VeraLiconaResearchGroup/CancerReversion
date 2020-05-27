# Compare network from geneXplain to paritally corrected network

def main():
    old = open("MRs to TFs step7 _expr.sif").read().split('\n')
    new = open("MRs to TFs step7_CORRECT.sif").read().split('\n')

    n = 0
    print("Check:")
    for line in old:
        row = line.split('\t')
        for edge in new:
            row2 = edge.split('\t')
            if row[0] == row2[0] and row[2] == row2[2]:
                if row[1] == row2[1]:
                    print(line)
                if row[1] != row2[1]:
                    n += 1

    print("number of changed edges: ", n)

main()

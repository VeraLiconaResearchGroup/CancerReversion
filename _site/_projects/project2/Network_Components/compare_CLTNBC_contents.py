# exploring weighted sums

def unique(list, thing):
    if thing not in list:
        list.append(thing)

def main():
    DEG = open('FunDEGs_ranked_Zscore/FunDEGs_rankDEGs_zscore_pvalFDR_4652').read().split('\n')
    FOC = open('FunDEGs_ranked_Zscore/FunDEGs_FOC_LCC_noHKG_80').read().split('\n')
    SOC = open('FunDEGs_ranked_Zscore/FunDEGs_SOC_exprnoHKG_316.txt').read().split('\n')
    HOC = open('EMT_innateimmune.txt').read().split('\n')
    CL = open('CL_genes.txt').read().split('\n')
    BDO = open('breast_DO.txt').read().split('\n')


    HOC_SOC = []
    CL_SOC = []
    BDO_SOC = []
    HOC_FOC = []
    CL_FOC = []
    BDO_FOC = []

    missed = []
    
    for node in SOC:
        if node in HOC:
            HOC_SOC.append(node)
        if node in CL:
            CL_SOC.append(node)
        if node in BDO:
            BDO_SOC.append(node)

    for node in FOC:
        if node in HOC:
            HOC_FOC.append(node)
        if node in CL:
            CL_FOC.append(node)
        if node in BDO:
            BDO_FOC.append(node)

    i = 0
    j = 0
    k = 0

    print("Missing from HOC:")
    for node in HOC_SOC:
        if node not in HOC_FOC:
##            print(node)
            unique(missed, node)
            i += 1
    print(i)
    print("Missing from CL:")
    for node in CL_SOC:
        if node not in CL_FOC:
##            print(node)
            unique(missed, node)
            j += 1
    print(j)
    print("Missing from BDO:")
    for node in BDO_SOC:
        if node not in BDO_FOC:
##            print(node)
            unique(missed, node)
            k +=1
    print(k)

    print('Total missed:',len(missed))

main()

# Compare VCF and COSMIC

import re

def main():
    # want to print lines in VEP where AA change doesnt match COSMIC
    vcf = open('231_SNV_COSMIC_output.vcf').read().split('\n')
    vcf_otherstrand = open('231_otherstrand_output.vcf').read().split('\n')
    correct = open('Gene_AA_CORRECT').read().split('\n')
    i = 0
    k = 0
    vcf_names = [] # the orig vcf file has the right data for these nodes
    vcf_otherstrand_names = [] # the vcf with switched bases has the right data for these nodes
    temp = []
    temp2 = []
    ls = []
    
    for lines in vcf:
        line = lines.split('\t')
        temp.append(line[0])
        for entry in correct:
            row = entry.split('\t')
            temp2.append(row[0])
            if line[0] == row[0] and line[10] == row[1]:
                i += 1
                vcf_names.append(row[0]) 
##                print(line) # get VEP output line
                
    for lines in vcf_otherstrand:
        line = lines.split('\t')
        ls.append(line[0])
        for entry in correct:
            row = entry.split('\t')
            if line[0] == row[0] and line[10] == row[1]:
                i += 1
                vcf_otherstrand_names.append(row[0]) 
##                print(line) # get VEP output line


##    for name in vcf_names: #Checking overlap between two lists
##        if name in vcf_otherstrand_names:
##            k += 1
##            print(name)
##    print(k) #k = 0 --> no overlap

    NOTinVCF = [] #to get everything I missed in the correct file (ranom insertions and deletions)
    for name in temp:
        if name not in temp2:
            NOTinVCF.append(name)
##    print(NOTinVCF)
    NOTinOTHER = [] # doesn't have anything 
    for name in ls:
        if name not in temp2:
            NOTinOTHER.append(name)
##    print(NOTinOTHER)

    nodata = ['AHNAK','AHNAK_ENST00000257247','AKAP2','C20orf141','C9orf131','CHD5_ENST00000262450','CLDN16','CLSPN','CLSPN_ENST00000251195','CNDP1','CUL9','FASTKD1','FTSJD1','GPR39','HAVCR1','M6PR','MAP1A','OR2C1','OR5J2','PALM2-AKAP2','PKD1L2','PKD1L2_ENST00000525539','PON2','PPP1R12B','SDK1','SMR3B','TRIM41','TRIM65','ZNF295']

    for lines in vcf: #getting VEP output for what I missed
        line = lines.split('\t')
        for name in nodata:
            if name == line[0]:
                pass
##                print(line)

    prtn = open('damaged_proteins').read().split('\n')
    orig = []
    other = []
    for name in prtn:
        if name in vcf_names:
##            print("orig:", name)
            orig.append(name)
        elif name in vcf_otherstrand_names:
##            print("other:", name)
            other.append(name)
        elif name in nodata:
##            print("orig:", name)
            orig.append(name)
        else:
            print("neither:", name)

    vcf_vcf = open('231_SNV_COSMIC.vcf').read().split('\n')
    vcf_otherstrand_vcf = open('231_otherstrand.vcf').read().split('\n')

    vcf_unique = []
    for x in vcf_names:
        if x not in vcf_unique:
            vcf_unique.append(x)
##    print(vcf_unique)

    other_unique = []
    for x in vcf_otherstrand_names:
        if x not in other_unique:
            other_unique.append(x)
##    print(other_unique)

    for line in vcf_vcf:
        for name in vcf_unique:
            if re.search(r'\b' + name + r'\b', line):
                print(line)
        for name in nodata:
            if re.search(r'\b' + name + r'\b', line):
                print(line)
    for line in vcf_otherstrand_vcf:
        for name in other_unique:
            if re.search(r'\b' + name + r'\b', line):
                print(line)

main()

# Identify "good" perturbations

def main():
    quantDAC = open("quantifier_DAC_FC2.txt").read().split('\n')
    quant = open("quantifierFC2.txt").read().split('\n')
    FC = open("FC2").read().split('\n') # Read in FC nodes
    basal = open("FC2_231_basal").read().split('\n') # read in basal values of the FC nodes for our cancerous cell line
    good = [] #list of perturbations with the right direction of activity sign for all 8 readout nodes
    
    for line in quantDAC: #get list of number of successful perturbations
        row = line.split(' ')
        if row[-1] == '8':
            temp = row[0].split('_')
            num = temp[2][:4]
            good.append(num)
                    
    perturbs = {} #Dictionary of the nodes that were actullay perturbed (initial state different than its level in the basal file) for each successful perturbation
    i = 0
    nums = {} #Dictionary of the number of perturbed nodes for each successful perturbation
    state = {}
    for n in good:
        p = []
        s = []
        m = 0
        i = 0
        file = open("FCbasal_perturbation/FC_perturbation_" + n + ".txt").read().split('\n') # read in successful perturbation file
        while i <= 7:
            thing= basal[i].split('\t')
            if thing[1] != file[i]: # if node is perturbed
                p.append(FC[i])
                m += 1
                if file[i] == '-1':
                    s.append('inhibited')
                elif file[i] == '0':
                    s.append('0')
                elif file[i] == '1':
                    s.append('activated')
            i += 1
        perturbs[n] = p
        nums[n] = m
        state[n] = s
            

    strong = [] # initialize list of perturbations that give right DAC on all RONs and filp at least one signs
    flips = {}
    for line in quant:
        row = line.split(' ')
        for num in good:
            if row[0] == "FC2_perturbation_" + str(num) + ":" and row[1] != '0':
                strong.append(num)
                flips[num] = row[1]
##    print("Perturbation Number\tNumber of flipped signs\tNumber of Perturbed Nodes\tPerturbed Nodes\tStatus of Perturbed Nodes")
##    for num in strong:
##        print(num + '\t' + str(flips[num]) + '\t' + str(nums[num]) + '\t' + str(perturbs[num]) + '\t' + str(state[num]))

    outputfile=open('strong_perturbations_FC2.txt','w+')
    outputfile.write("Perturbation Number\tNumber of flipped signs\tNumber of Perturbed Nodes\tPerturbed Nodes\n")
    n = 0
    for num in strong:
        outputfile.write(num + '\t' + str(flips[num]) + '\t' + str(nums[num]) + '\t')
        while n < nums[num]:
            outputfile.write(str(perturbs[num][n]) + ' (' + str(state[num][n]) + ')' + ', ')
            n +=1 
        outputfile.write('\n')
        n = 0

    outputfile.close()


##    
##    for key, value in nums.items() :
##        if value == 3:
##            print(key)
    
main()
    

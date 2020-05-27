import os
import sfa
import numpy as np
import networkx as nx
import random
from pathlib import Path


numperturbations = 3 ** 8  #Number of possible combinations
FCset = "FC2"

class ThreeNodeCascade(sfa.base.Data):
    def __init__(self):
        super().__init__()
        self._abbr = "TNC"
        self._name = "A simple three node cascade"

        # Specify the file path for network file in SIF.
        dpath = os.path.dirname(__file__)
        fpath = os.path.join(dpath, '../../Network Construction 2/Network_full.sif')
        # Use read_sif function.
        signs = {'activates':1, 'inactivates':-1}
        A, n2i, dg = sfa.read_sif(fpath, signs=signs, as_nx=True)
        self._A = A
        self._n2i = n2i
        self._dg = dg
        self._i2n = {idx: name for name, idx in n2i.items()}
        
    # end of def __init__
# end of def class

if __name__ == "__main__":
##    initalize SF Class
    data = ThreeNodeCascade()
    algs = sfa.AlgorithmSet()
    alg = algs.create('SP')
    alg.data = data
    alg.params.apply_weight_norm = True
    alg.initialize()
    

    n = data.dg.number_of_nodes() #the number of nodes
    b = np.zeros((n,))
###################INPUT FILES
#readout nodes
#readout node steady state values
#readout node sslogFC values
#network nodes
#network node state file
#FC set
##read in readout nodes, readout node attractor state file
    ronfile='rons_8'
    readout_nodes=open(ronfile).read().split('\n')

    ronssfile='rons_ss'
    readout_nodes_state_file=open(ronssfile).read()

    ronlogFCfile='rons_8_logFC'
    readoutnodes_logFC_file=open(ronlogFCfile).read()

##  read in full network nodes, and their initial conditions (normalized expression)
    network=open('expression_nodes_114').read().split('\n')   
    attractor1_file='231_basal'
    networkstatesfile=open(attractor1_file).read()
    j=0
    g=0

##  read in FC nodes
    FC=open(FCset).read().split('\n')


## read in ideal LogFC direction
    #logFCfile=comparison_folder/'t2resvveh_logFC.txt'
    #logFCread=open(logFCfile).read()

#######################################


    
##  create list of node states (normexp)

    nwstates=networkstatesfile.split('\n') #create list of initial state file
    num_readouts=len(readout_nodes)
    print(num_readouts)   
    for node in network:
        #print(node)
        nw_state=float(nwstates[0])
        b[data.n2i[node]]=nw_state #set node to it's initial state
        nwstates.pop(0)


    readout_dict={} #initialize dict for readout nodes values
    fullnetwork_dict={}
    n=1
    quantifierout=open('quantifier' + FCset + '.txt','w+')
    logquantifierout=open('quantifier_DAC_' + FCset + '.txt','w+')
    while n<=numperturbations:
        #create list of the readout node attractor states
        readout_node_state=readout_nodes_state_file.split('\n')
        #create list of ideal logFC
        readout_node_logFC=readoutnodes_logFC_file.split('\n')
        

##  Set FC nodes to randomized activation and inhibitions
        FCdict={}
        FCstates=open('FCbasal_perturbation/FC_perturbation_'+ str(n).rjust(len(str(numperturbations)), '0') + '.txt').read().split('\n')
        for FCnode in FC:
            fc_state=float(FCstates[0])
            b[data.n2i[FCnode]]=fc_state
            FCstates.pop(0)
            
            
##  SFA
        x = alg.compute(b)
       
        
        
        quantifier=0
        logFCquantifier=0
##  clear readout dict and simulation dict so it can hold this iteration's results
        readout_dict={} 
        foldchangeDict={}
        for i, act in enumerate(x): #for all nodes (i) and their activity (act) in network
           istr=str(data.i2n[i]) #get node name
##  if i is a readout node, save values to readout_dict, and compare values to logFC
           if istr in readout_nodes: #if this is  a readout node
               readout_dict[istr]=act #set readoutnode value to activity
               given_state=float(readout_node_state[0])#get the attractor state of the readout node
               given_logFC=float(readout_node_logFC[0])
               

               logFC=round((given_state-act),5)
               foldchangeDict[istr]=logFC

               if given_state<0 and act>0:
                   quantifier=quantifier+1
               if given_state>0 and act<0:
                   quantifier=quantifier+1
               readout_node_state.pop(0)
               if given_logFC<0 and logFC<0:
                   logFCquantifier+=1
               if given_logFC>0 and logFC>0:
                   logFCquantifier+=1
               readout_node_logFC.pop(0)
           fullnetwork_dict[istr]=act
           
        
        outputfile=open('SFAoutput' + FCset + '/SFAoutput_ron_' + FCset + '_'+str(n).rjust(len(str(numperturbations)), '0')+'.txt','w+') #SFA results
        outputfile.write('stead state value\tlogFC\n')
        for k,v in readout_dict.items():
            logFCval=foldchangeDict[k]
            #print(logFCval)
            outputfile.write(str(v)+'\t'+str(logFCval)+'\n')
    

        fullnetworkout=open('SFAoutput' + FCset + '/SFAoutput_full_' + FCset + '_'+str(n).rjust(len(str(numperturbations)), '0')+'.txt','w+')
        for key1,val1 in fullnetwork_dict.items():
            fullnetworkout.write(str(key1)+'\t'+str(val1)+'\n')
            
           
        quantifierout.write(FCset + '_perturbation_'+str(n).rjust(len(str(numperturbations)), '0')+': '+str(quantifier)+'\n')
        logquantifierout.write(FCset + '_perturbation_'+str(n).rjust(len(str(numperturbations)), '0')+': '+str(logFCquantifier)+'\n')
      
        outputfile.close()
        fullnetworkout.close()
        n+=1
                        
          
    quantifierout.close()
    logquantifierout.close()




##    b[data.n2i['EGF']] = 1
##    xs1=alg.compute(b)
##    outputfile.close() 
##        
##    for i, act in enumerate(x):
##           outputfile.write("%s %f"%(data.i2n[i], act))
##           outputfile.write('\n')
##    outputfile.close()

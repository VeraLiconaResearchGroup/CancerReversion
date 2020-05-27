from libsbml import *
import csv
def get_sign(annotations):
    for annotation in annotations:
        for signline in annotation:
            if 'Reaction label' in signline:
                #print(signline)
                signline=signline.strip().split('(')
                sign=signline[-1].replace(')"/>','')
                if sign=="+":
                    edge='activates'
                if sign=='-':
                    edge='inactivates'
                return edge
    

def main():
    reader=SBMLReader()
    document=reader.readSBML('MRs expressed prtn viz all.xml')
    Model=document.getModel()
    numspecies=Model.getNumSpecies()
    print(numspecies)
    
    numreactions=Model.getNumReactions()
    print(numreactions)
    IDlist=[]
    modformdict={}
    complexdict={}
    litdict={}
    
## Processing Species
    for z in range(0,numspecies):
        species=Model.getSpecies(z)
        
        ID=species.getIdAttribute()
        name=species.getName()
        IDlist.append(ID)
        annot=species.getAnnotationString().split('\n')
        i=0
        for line in annot:
            if '<rdf:Bag>' in line:
                rdfstart=i+1
            if '</rdf:Bag>' in line:
                rdfend=i
            
            if '<property elementType="String" name="complexes"' in line:
                complexstart=i+1
                j=i            
                complexline=annot[j]
                while '</property' not in complexline:
                    j+=1
                    complexline=annot[j]
                complexend=j
            if '<property elementType="String" name="modifiedForms"' in line:
                modstart=i+1
                
                k=i            
                modline=annot[k]
                while '</property' not in modline:
                    k+=1
                    modline=annot[k]
                modend=k    

            i+=1



        rdflines=annot[rdfstart:rdfend]
        for rdf in rdflines:
            if 'pubmed#' in rdf:
                resource=rdf.split('#')
                PMID=resource[1].strip('"/>')
                litdict.setdefault(ID,[]).append(PMID)
                
        complexlines=annot[complexstart:complexend]
        for molcomplex in complexlines:
            complexparts=molcomplex.strip().split(':')
            complexMO=complexparts[0].replace('<item>','')
            complexdict.setdefault(ID,[]).append(complexMO)
            
        modifiedlines=annot[modstart:modend]
        
        for mods in modifiedlines:
            modparts=mods.strip().split(':')
            modMO=modparts[0].replace('<item>','')
            modformdict.setdefault(ID,[]).append(modMO)


##Processing Reactions

    edgelist=[]
    for x in range(0,numreactions):
        reaction=Model.getReaction(x)
        reactantnum=reaction.getNumReactants()
        productnum=reaction.getNumProducts()
        modifiernum=reaction.getNumModifiers()

        if productnum==0:
            annotations=[]
            for i in range(0,modifiernum):
                sourcelist=[]
                annotations.append(reaction.getListOfModifiers().get(i).getAnnotationString().split('\n'))
                sourcelist.append(reaction.getListOfModifiers().get(i).getSpecies())
            for i in range(0,reactantnum):
                targetlist=[]
                annotations.append(reaction.getListOfReactants().get(i).getAnnotationString().split('\n'))
                targetlist.append(reaction.getListOfReactants().get(i).getSpecies())
            edge=get_sign(annotations)
            if len(sourcelist)>len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
            if len(targetlist)>len(sourcelist):
                for i in targetlist:
                    target=i
                    for j in sourcelist:
                        source=j
                        line=source,target,edge
                        edgelist.append(line)            
            if len(sourcelist)==len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
        if reactantnum==0:
            annotations=[]
            for i in range(0,modifiernum):
                sourcelist=[]
                annotations.append(reaction.getListOfModifiers().get(i).getAnnotationString().split('\n'))
                sourcelist.append(reaction.getListOfModifiers().get(i).getSpecies())
            for i in range(0,productnum):
                targetlist=[]
                annotations.append(reaction.getListOfProducts().get(i).getAnnotationString().split('\n'))
                targetlist.append(reaction.getListOfProducts().get(i).getSpecies())
            edge=get_sign(annotations)
            if len(sourcelist)>len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
            if len(targetlist)>len(sourcelist):
                for i in targetlist:
                    target=i
                    for j in sourcelist:
                        source=j
                        line=source,target,edge
                        edgelist.append(line)            
            if len(sourcelist)==len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
        if modifiernum==0:
            annotations=[]
            for i in range(0,reactantnum):
                sourcelist=[]
                annotations.append(reaction.getListOfReactants().get(i).getAnnotationString().split('\n'))
                sourcelist.append(reaction.getListOfReactants().get(i).getSpecies())
            for i in range(0,productnum):
                targetlist=[]
                annotations.append(reaction.getListOfProducts().get(i).getAnnotationString().split('\n'))
                targetlist.append(reaction.getListOfProducts().get(i).getSpecies()) 
            edge=get_sign(annotations)
            if len(sourcelist)>len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
            if len(targetlist)>len(sourcelist):
                for i in targetlist:
                    target=i
                    for j in sourcelist:
                        source=j
                        line=source,target,edge
                        edgelist.append(line)            
            if len(sourcelist)==len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
        if reactantnum>0 and productnum>0 and modifiernum>0:
            annotations=[]
            for i in range(0,reactantnum):
                sourcelist=[]
                annotations.append(reaction.getListOfReactants().get(i).getAnnotationString().split('\n'))
                sourcelist.append(reaction.getListOfReactants().get(i).getSpecies())
            for i in range(0,modifiernum):

                annotations.append(reaction.getListOfModifiers().get(i).getAnnotationString().split('\n'))
                sourcelist.append(reaction.getListOfModifiers().get(i).getSpecies())
            for i in range(0,productnum):
                targetlist=[]
                annotations.append(reaction.getListOfProducts().get(i).getAnnotationString().split('\n'))
                targetlist.append(reaction.getListOfProducts().get(i).getSpecies()) 
            edge=get_sign(annotations)
            if len(sourcelist)>len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line)
            if len(targetlist)>len(sourcelist):
                for i in targetlist:
                    target=i
                    for j in sourcelist:
                        source=j
                        line=source,target,edge
                        edgelist.append(line)            
            if len(sourcelist)==len(targetlist):
                for i in sourcelist:
                    source=i
                    for j in targetlist:
                        target=j
                        line=source,target,edge
                        edgelist.append(line) 
##associating literature with edges
    edgelitlist=[]
    for edge in edgelist:
        lits=[]
        source=edge[0]
        target=edge[1]
        if source in litdict:
            sourcelit=litdict[source]
        if target in litdict:
            targetlit=litdict[target] 
        if len(sourcelit)>0 and len(targetlit)>0:
            for lit in sourcelit:
                for litt in targetlit:
                    if lit==litt:
                        lits.append(lit)
        thing=source,target,edge[2],lits
        edgelitlist.append(thing)
##    for item in edgelitlist:
##       print (item)
##                    
##    for item in IDlist:
##        print(item)

    with open('edgelit', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\n')
        wr.writerow(edgelitlist)
    with open('edges.csv', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\n')
        wr.writerow(edgelist)
    with open('MOs', 'w') as myfile:
        wr = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter='\n')
        wr.writerow(IDlist)

        
    
main()

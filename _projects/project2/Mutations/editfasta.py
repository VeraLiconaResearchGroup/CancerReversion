# ----------------------
# editfasta.py removes unneccesary new line characters from the output reference.fa and mutant.fa from ensembl VEP with the
# protein seqs plug-in and returns mut1.fa and ref1.fa without them.
# ----------------------

import re
def main():
    with open('reference.fa',"r") as newFile:
        sequences=newFile.read()
        sequences=re.split("^>", sequences, flags=re.MULTILINE)
    del sequences[0]
    with open('ref1.fa',"w") as newFasta:
        for fasta in sequences:
            header,sequence=fasta.split('\n',1)
            header = ">" + header + "\n"
            sequence = sequence.replace("\n","") + "\n" 
            newFasta.write(header + sequence)
    newFasta.close()

    with open('mutated.fa',"r") as newFile:
        sequences=newFile.read()
        sequences=re.split("^>", sequences, flags=re.MULTILINE)
    del sequences[0]
    with open('mut1.fa',"w") as newFasta:
        for fasta in sequences:
            header,sequence=fasta.split('\n',1)
            header = ">" + header + "\n"
            sequence = sequence.replace("\n","") + "\n" 
            newFasta.write(header + sequence)
    newFasta.close()
main()


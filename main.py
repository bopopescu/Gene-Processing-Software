import re
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Fasta file")
flag = 1
i = -1
info = []
gene_sequence = []
length=[]
countOfA=[]
countOfC=[]
countOfG=[]
countOfT=[]
# def callback():
#     global name
#     name = filedialog.askopenfilename()
#     print(name)

# Reading the file and seperating the information and gene sequence
def read_file():
    name = filedialog.askopenfilename()
    global i, info, gene_sequence
    messagebox.showinfo("Confirmation message", "this file has been successfully uploaded")
    with open(name, "r") as f:
        for line in f:
            if line[0] == '>':
                line = line.rstrip('\n')
                info.append(line.strip('>'))
                i = i + 1
                gene_sequence.append("")
                length.append(0)
                countOfA.append(0)
                countOfC.append(0)
                countOfG.append(0)
                countOfT.append(0)
            elif (bool(re.match('^[AGCT]', line))):
                gene_sequence[i] = gene_sequence[i] + line.strip()
                length[i]=len(gene_sequence[i])
                countOfA[i]= gene_sequence[i].count('A')
                countOfC[i] = gene_sequence[i].count('C')
                countOfG[i] = gene_sequence[i].count('G')
                countOfT[i] = gene_sequence[i].count('T')
            else:
                # print("Either gene sequence contains letters other than AGCT or specification takes more than one line.")
                # print("Incorrect Fasta file.")
                flag = 0
                messagebox.showinfo("Error message", "this file is not in fasta format")
                sys.exit(1)


# Writing the output file in the speified format
def download_file():
    global i
    with open("Output.txt", "w") as fd:
        fd.write('{0:5}  {1:100}  {2}   {3} {4} {5} {6} {7}\n'.format("Sl. No.", "Info", "Gene","length","Count-A","Count-C","Count-G","Count-T"))

        for iter in range(0, i+1):
            fd.write('{0:5} {1:100} {2} {3} {4} {5} {6} {7}\n'.format(str(iter + 1), str(info[iter]), str(gene_sequence[iter]),str(length[iter]),str(countOfA[iter]),str(countOfC[iter]),str(countOfG[iter]),str(countOfT[iter])))




Button(text = "Open File", command = read_file).pack(fill = X)

if flag:

    Button(text = "Download File", command = download_file).pack(fill = X)
else:
    text = Text(Tk)
    text.insert(END, "Either gene sequence contains letters other than AGCT or specification takes more than one line.\nIncorrect Fasta file.\n")

root.mainloop()
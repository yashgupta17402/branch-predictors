#static branch predictor
#Written by Pranav Bhutada(IMT2021105) Yogesh Goyal(IMT2021542) Yash Gupta(IMT2021514)
from prettytable import PrettyTable
my_output=PrettyTable(["Static prediction","Percentage of Misprediction"])
file=open('file0.txt','r') #Trace file reading
total_branches=0
branches_not_taken=0
branches_taken=0
pc_binary=[] #contains binary form of pc 32 bits
for each in file:
    lst=each.split()
    pc_binary.append('{:032b}'.format(int(lst[0])))
    total_branches+=1
    if(lst[1]=='N'): branches_not_taken+=1
    else: branches_taken+=1
file.close()
# for i in pc_binary:
#     print(i)
misprediction_rate=(branches_not_taken/total_branches)*100
my_output.add_row(["Always Taken",misprediction_rate])
my_output.add_row(["",""])
misprediction_rate=(branches_taken/total_branches)*100
my_output.add_row(["Always Not Taken",misprediction_rate])
print(my_output)


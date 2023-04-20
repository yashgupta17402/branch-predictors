#dynamic branch predictor
#Written by Pranav Bhutada(IMT2021105) Yogesh Goyal(IMT2021542) Yash Gupta(IMT2021514)
from prettytable import PrettyTable
my_output=PrettyTable(["Log of predictor size","Percentage of Misprediction"])

def twobit_dbp(n):
    file=open('file0.txt','r')
    pc_binary=[]
    for each in file:
        lst=each.split()
        pc_binary.append('{:032b}'.format(int(lst[0])))
    # print(pc_binary)
    BHT=[]
    total_branches=0
    mispredictions=0
    misprediction_rate=0
    ctr=0
    correct_predictions=0
    for i in range (0,pow(2,n)):
        x=('{:032b}'.format(i))
        BHT.append([x[-n:],"00"])
    file.close()
    file=open('file0.txt','r')
    for each1 in file:
        
        lst=each1.split()
        y=pc_binary[ctr]
        ctr+=1
        y=y[-n:]
        x=int(y,2)
        if(BHT[x][1]=='00'):
            if(lst[1]=='N'):
                BHT[x][1]='01'
                mispredictions+=1
        elif(BHT[x][1]=='01'):
            if(lst[1]=='T'):
                 BHT[x][1]='00'
            else:
                BHT[x][1]='10'
                mispredictions+=1
        elif(BHT[x][1]=='10'):
            if(lst[1]=='T'):
                BHT[x][1]='01'
                mispredictions+=1
            else:
                BHT[x][1]='11'
        elif(BHT[x][1]=='11'):
            if(lst[1]=='T'):
                BHT[x][1]='10'
                mispredictions+=1
        total_branches+=1
    misprediction_rate=(mispredictions/total_branches)*100
    my_output.add_row([n,misprediction_rate])
    file.close()
   
for i in range(2,21):
    twobit_dbp(i)
    
print(my_output)
        
              
                
                
        

import sys
sys.setrecursionlimit(80000)
#80.000 - is not a const and mary vary depending on input's size

def CheckProperty(cur_id, curLen):
    global TotalLen
    global  AnswerFlag

    if cur_id==-1:
        curLen+=1
        if TotalLen==-1:
            TotalLen=curLen;
        else:
            if TotalLen!=curLen:
                AnswerFlag=0
    else:
        if value_arr[cur_id]!=1:
            curLen+=1
        # proverka na chernih detey krasnoy vershiny
        elif (value_arr[childL_arr[cur_id]]==1 or value_arr[childR_arr[cur_id]]==1):
            AnswerFlag=0
        CheckProperty(childL_arr[cur_id],curLen)
        CheckProperty(childR_arr[cur_id],curLen)

value_arr=[]
childL_arr=[]
childR_arr=[]
possibe_root_arr=[]

n=int(input())

for i in range(0,n):
    possibe_root_arr.append(i)

for i in range (0,n):
    list=input().split()

    if int(list[0])==0:
        childL_arr.append(-1)
        childR_arr.append(-1)
        value_arr.append(int(list[1]))
    if int(list[0])==1:
        childL_arr.append(-1)
        childR_arr.append(int(list[1]))
        value_arr.append(int(list[2]))
        possibe_root_arr.remove(int(list[1]))
    if int(list[0])==2:
        childL_arr.append(int(list[1]))
        childR_arr.append(int(list[2]))
        value_arr.append(int(list[3]))
        possibe_root_arr.remove(int(list[1]))
        possibe_root_arr.remove(int(list[2]))


value_arr.append(-1)

TotalLen=-1
AnswerFlag=1

if value_arr[0]==1:
    AnswerFlag=0
else:
    CheckProperty(possibe_root_arr[0],0)

if !AnswerFlag:
    print("NO")
else:
    print("YES")
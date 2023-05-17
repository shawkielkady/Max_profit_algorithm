# Max_profit_algorithm
maxprofits=[0,0,0,0]
tasks=[]
explain the loops (the heart of the algorithm)
when i=0 (1,6,6)
j =-1 it canot so will ignore second loop becaue j=i-1
tasks=[[0]]
maxprofits =[6]
#####################################################
when i=1 (2,5,5)
j=0
6 <= 5 ?
no so i canot do if statement
tasks=[[0],[1]]
maxprofits=[6,5,0,0]
#####################################################
when i=2 (5,7,5)
j=0,1
j=0:
6 <= 5 (skip)
j=1 , i=2
5 <= 5 so if statement will be done
tasks[2]= tasks[1]=[1,2]
maxprofits =[6,5,10,0]
################################################
i= 3 (6,8,3)
j=0,1,2
j=0 , i=3 (1,6,6) , (6,8,6)
6 <= 6 so if statement will be done
tasks[3]=[0,3]
maxprofits[i]=9
maxprofits=[6,5,10,9]
########################################
at the end 
maxprofits=[6,5,10,9]
tasks non-overlapping=[[0],[1],[1,2],[0,3]]
##############################################
output after running the code:
The maximum profit is  10
The jobs involved in max profit are (2, 5, 5) (5, 7, 5) 










tupleList = list(tuple(map(int,input('enter values of tuple:').split(','))) 
           for p in range(int(input('enter no of tuples: ')))) # here first we need to enter the no of tuples being given as input
final=[]
#input the value to be removed
a=int(input('enter the value to be removed: '))
for i in range(len(tupleList)):
    if tupleList[i][0]==a or tupleList[i][1]==a:
        continue
    else:
        final.append(tupleList[i])
print(final)


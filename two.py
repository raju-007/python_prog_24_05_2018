def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[-5:])


printList()
print("$$$$$$$$$$")
tp=[1,2,3,4,5,6,7,8,9,10]
ki=[]
ji=[i for i in tp if i%2==0 ]
print (ji)
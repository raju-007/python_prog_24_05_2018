li = [1,2,3,4,5,6,7,8,9,10]

squaredNumbers =list(map(lambda x: x**2, range(1,11))) #range or li
print (squaredNumbers)
print('!!!!!!!!!!!!!!')
evenNumbers = list(filter(lambda x: x%2==0, range(1,21)))
print (evenNumbers)
print("$$$$$$$$$$$$$$")
u=list(map(lambda s:s**2,li))
print (u)
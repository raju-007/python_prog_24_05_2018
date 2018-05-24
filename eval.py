import random
r=input("enter value  ")
print(eval(r))
print("##########random number ##6##########")
print (random.random()*100)
print("$$$$$$$$$$$$$$$")
print (random.random()*100-5)
print (random.choice([i for i in range(11) if i%2==0]))
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
li=[1,5,3,8,9,4,44,7,677,99,54,36,95,394,43]
print(random.sample(li,5))
print("###############")
print (random.sample([i for i in range(1,100000) if i%5==0 and i%7==0], 100))
print("************************")
print (random.randrange(7,16))




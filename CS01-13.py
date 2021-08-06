A=[]
while (True):
    i=int(input("ใส่เกรดของคุณ "))
    if i == -1 : 
       break
    A += [i]
    print("เกรดของคุณคือ ",i)
print(A)
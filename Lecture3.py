tup = (1,4,9,16,25,36,49,64,81,100)
# if (tup.count(9)==1):
#     print("number found")
# else:
#     print("not found")


i=0
x=4
while (i<10):
    if (x==tup[i]):
        print("number found at index: ",i)
    else:
        print("number not found at index: ",i)
    i+=1

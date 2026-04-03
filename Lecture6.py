def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print("Using function without recursion: ",sum_natural(10))
###################################
def sum_natural(n):
    if (n==0):
        return 0
    return n+sum_natural(n-1)
print("Using function with recursion: ",sum_natural(10))
###################################
ls = [1,32,43,76,51,16]
def list_el():
    for i in range(1,len(ls)):
        print(ls[i],end=" ")
        #return i
print(list_el())
###################################
lst1 = [11,32,43,76,51,16]
def list_el(ls,i):
    if (i==len(ls)):
        return
    print(ls[i])
    list_el(ls,i+1)

list_el(lst1,0)

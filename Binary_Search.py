def bin_search(y, x):

    low=0

    high= len(y)-1

    middle=0

    while low<=high:

        middle=(high+low)//2

        if x>y[middle]:

            low=middle+1

        elif y[middle]>x:
            high=middle-1

        else:

            return middle

    return -999

n=int(input("Enter the number of integers in the array: "))
arr=[]   
for i in range(n):
    arr.append(int(input("Enter the element: ")))
arr.sort()
print(arr)
m=int(input("Enter the number to be searched in the array: "))

pos = bin_search(arr,m)

if pos == -1:
    print("Element not found")
else:
    print("Index position of the element: ",pos)

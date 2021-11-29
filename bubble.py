x=int(input("Enter number of students: "))
x=len(list)
for i in range(0, x-1):
    j=i+1
    if j < x:
        for j in range(i+1, x):
            if list[j] < list[i]:
                temp=list[j]
                list[j]=list[i]
                list[i]=temp

                print(list)
                print(list[:5])
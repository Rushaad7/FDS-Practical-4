
x = [64, 25, 12, 22, 11]
for i in range(len(x)):
     min_idx = i
     for j in range(i+1, len(x)):
        if x[min_idx] > x[j]:
            min_idx = j
              
     
            x[i], x[min_idx] = x[min_idx], x[i]
  

print ("Array is now sorted")
for i in range(len(x)):
    print(x[i]), 
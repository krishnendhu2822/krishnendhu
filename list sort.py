l1=[2,4,9,-10,100,1000,89,67,1,3,0,98]
l2=set(l1)
print(l1)
print(l2)
l3=list(l2)
l3.sort()
print("second largest",l3[-2])
print("second smallest",l3[1])
      

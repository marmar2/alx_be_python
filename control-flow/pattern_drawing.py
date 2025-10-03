size=int(input("Enter the size of the pattern:"))
i=1
while i<size+1:
   i+=1
   for j in range(size+1):
      j+=1
      print("*", end="") 
   print("\n")  
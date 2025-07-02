file = input("Enter the filename: ")
try:
   fread = open(file, "r")
except FileNotFoundError:
   print("File not found")
   exit()
lines = fread.readlines()
for i in range(len(lines)):
   print("Line " , str(i+1) , ": " , lines[i], end = "")
print("")
num = int(input("Enter a line number: "))
while num != 0:
   print("Line " , str(num) , ": " , lines[num-1], end = "")
   if num == 9:
       print("")
   num = int(input("Enter a line number: "))
else:
   exit()
fread.close()

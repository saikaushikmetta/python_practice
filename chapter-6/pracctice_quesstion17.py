# Write a program using nested loops to print this pattern:
# *
# * *
# * * *
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
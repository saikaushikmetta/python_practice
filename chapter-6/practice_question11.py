# 11.Write a program that prints the multiplication table of any number entered by
# the user using a for loop.
# Example Output:

# Enter number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# ...
# 6 x 10 = 60
n=int(input("enter the number that you want a table for"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)

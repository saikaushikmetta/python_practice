# Mini Project – Multiplication Table
# Goal: Print the multiplication table of a number using a loop.
# Sample Run:
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
n=int(input("enter the number that you want a table for"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
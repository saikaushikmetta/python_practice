#write a program that prints the sum of first n natural numbers
#for example, if n=5, then output should be 1+2+3+4+5=15
#(Hint: keep a running total inside the loop)
n=int(input("enter a number: "))
sum=0
while(n>=1):
    sum=sum+n
    n=n-1
print("sum= ",sum)
print("N= ",n)
#write a program to reaad a text from a given file certificate.txt and find whether it contains the word live
file=open("certificate.txt","r")
data=file.read()
for i in data:
    if i=="live":
        print("found live in the given file")
    else:
        print("not found")
file.close()
#another logic of it
file=open("certificate.txt","r")
data=file.read()
if "Live" in data:
    print("live word is there")
else:
    print("not found")
file.close()

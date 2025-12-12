#read only first line of bio.txt
with open("bio.txt","r") as f:
    data=f.readline()
    print(data)
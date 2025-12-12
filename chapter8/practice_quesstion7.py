#print how many lines are present in notes.txt
with open("notes.txt","r") as f:
    data=f.readlines()
    print("the lines present in the file 'note.txt are",len(data))
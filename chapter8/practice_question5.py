#read a file named story.txt and print the full content
with open("story.txt") as f:
    data =f.readlines()
    print(data)
    
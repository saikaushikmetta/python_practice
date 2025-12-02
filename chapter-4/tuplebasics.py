tup=(1,"kaushik",98,"kaushik")
print(tup)
#to access values in tuple we can acccesss them using index
print(tup[1])
#we cannot change its values using its index value
#tup[1]=78 causes error 
print(tup)
#empty tuples(interview question)
emptyTuple=()
single_tuple=(1,)#important
print(type(emptyTuple))
print(type(single_tuple))
print(tup.index("kaushik"))
print(tup.count("kaushik"))
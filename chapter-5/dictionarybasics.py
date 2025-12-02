#dictionary basics
dict={"name":"kaushik",
      "age":19,
      "city":"surat"
      }
print(dict)
print(type(dict))
print(id(dict))#stored memory location
#accessing value in dictionary
print(dict["name"])
#changing values using its key value
dict["name"]="shubham"
print("updated dictionary",dict)
#to add new key value 
dict["subject"]="python"
print(dict)
#to remove items
dict.pop("subject")
print(dict)
#funtions of dictionaries
dict.keys()
print(dict)
dict.values()
print(dict)
dict.items()
print(dict)
dict.get("name")
print(dict)
dict.update({"city":"surat"})
print(dict)
#nested dictionary
dict1 = {
    "name": "kaushik",
    "details": {
        "age": 18
    },
    "subject": "maths"
}

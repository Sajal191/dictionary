#Take two input list and then update the key list if it exist i=or else return key does not exist

data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(",")
list2=data2.split(",")
dict1=dict(zip(list1,list2))
key=input("key: ")
if key in dict1:
    val = input("value: ")
    dict1[key]=val
    print("sorted dictionary:",sorted(dict1.items()))
else:
     print("keys does not exist")

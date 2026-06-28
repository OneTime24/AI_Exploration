# basics


collec=[{
    "name":"ali",
    "age":18,
    "cgpa":3.5
},{
    "name":"ahmed",
    "age":13,
    "cgpa":3.4
},
{
    "name":"bilal",
    "age":20,
    "cgpa":3.9
},
]


# print(collec)


# for nam in collecs



def sum(*all):
    total=0;

    for i in all:
        total+=i
    
    return total

def total(**stuffs):

    total = 0

    for name, price in stuffs.items():
        total += price

    print("All Items:")

    for name, price in stuffs.items():
        print(f"{name} | {price}")

    return total


print(sum(1,2,3,4,5))


print(sum(5,4,1))



stuffs=[
    {"item":"pen",
     "price":20,
     },
     {"item":"paper",
      "price":50}
]


# print(stuffs)


for i in stuffs:
    print(i["item"])
    print(i["price"])


print(total(pen=20,paper=30,pencil=50))
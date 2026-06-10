

word="hello this is world"

print(word)

for wo in word:
    print(wo)


print("----------\n-------------")



print(word[0:6])

print(word[6:])

print(word[6:11])




word="B"+word[1:]

print(word)


print(word.find("world"))

word=word.replace("world","meow")

print(word)
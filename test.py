"""
msg = "Hello world"
print(msg)

splits=['Fleagle','Beagle','Drooper','Snorky']

for e in splits:
    print(e, end=":=> ")

print("\n")

text=input("type here: ")
for c in text:
    print(c)
"""

fruit=['avocados','bananas','oranges','grapes','mangos']

#print(", ".join(fruit))
#print(fruit)

for i, value in enumerate(fruit):
    print(i+1,value)

print("Sorting Program\n\n")

fruits = [
    "banana",
    "orange",
    "grapes",
    "strawberry",
    "blueberry",
    "raspberry",
    "peach",
    "pear",
    "plum",
    "cherry",
    "pineapple",
    "mango",
    "kiwi",
    "watermelon",
    "lemon",
    "lime",
    "papaya",
    "pomegranate",
    "avocado"
]
#python knows this is a list because of the brackets: [ ]
#commas seperate the items in the list
#quotes make whatever is inside them a string 

fruits.sort()
#fruits is the variable that is to be sorted, add that onto .sort() it will arrange each string alphabetically 


print("\nAlphabetical Order:\n")
for fruit in fruits:
    print(fruit)
#"for" tells python to go through the list one by one
#"in" tells python where to get the items from, which is the fruit list

print("""\n\nRecap:\n
"print()" is an output
"list" stores multiple items
".sort()" rearranges the list into alphabetical order
"for item in terms" loops through each item in the list

""")

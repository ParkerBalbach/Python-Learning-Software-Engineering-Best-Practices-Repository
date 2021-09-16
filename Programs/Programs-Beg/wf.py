import pprint

# Parker Balbach
# method to turn a list into a string
def listToString(s):
    str1=" "

    return (str1.join(s))


# opens file and reads it
file_object = open("Gettysburg-Address.txt", "r")

text = file_object.readlines()

# turn list to string in order to use replace and lower string methods
new_text = listToString(text)

# takes away punctuation
for char in ':;&!?_*-.,\n':
    new_text = new_text.replace(char,' ')
new_text = new_text.lower()

# splits txt and turns to list
word_list = new_text.split()

d = {}

# counts words
for word in word_list:
    d[word] = d.get(word, 0) + 1

# sort items: highest count first
sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)
pprint.pprint(sorted_d)





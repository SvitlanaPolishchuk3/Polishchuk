import re
a = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Let`s apply Capitalize. It will convert all letters to lowercase except for the first letter in the text
b = (a.capitalize())
print(b)

# Let`s replace 'iz' with 'is'. For pattern to work correct I add a space before iz:
c = (b.replace(' iz', ' is'))
print(c)

# My problem now that I have my sentences starting with lowercase. This script will split text in parts,
# then capitalize each sentence and after that join sentences in one text again.


def func_capitalize_sentences():
    sentences = c.split('.')
    final_senteces = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        sentence = sentence.capitalize()
        final_senteces.append(sentence)
    final_text = '. '.join(final_senteces)
    final_text1 = final_text+'.'
    return final_text1


print(func_capitalize_sentences())
n = func_capitalize_sentences()

# Now we need to create another sentence with last words of every sentence.
# This script will find all words that are followed by '.'
pattern = r'\w+\.'
test1 = (re.findall(pattern, n))
print(test1)

# This script will change our list back into string
test2 = ' '.join(test1)
print(test2)

# Now we can replace '.' with spaces and capitalize again.
d = (test2.replace('. ', ' '))
e = (d.capitalize())
print(e)

# Now we can join main text and our last sentence.
final_text2 = n + ' ' + e
print(final_text2)

# Also need to replace capital letter for 'this':
final_text3 = final_text2.replace("  this", "  This")
print(final_text3)

# We can use unicode symbol of whitespace to find all of them in the text.
testcount = (re.findall('\s', final_text2))

# Now we calculate them using 'len'
testcount1 = len(testcount)
print(testcount1)
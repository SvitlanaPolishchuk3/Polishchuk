import re


# Let`s create a function which will capitalize any text
def func_capitalize_param(a):
    func_capitaliz = a.capitalize()
    return func_capitaliz


x = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

func_capitaliz = func_capitalize_param(x)
print(func_capitaliz)


# Let`s replace 'iz' with 'is' using another function:
def func_replace_param(b, l, m):
    func_replac = b.replace(l, m)
    return func_replac


b = func_capitaliz
l = ' iz'
m = ' is'
func_replac = func_replace_param(b, l, m)
print(func_replac)


# Let`s create another function that will capitalize each sentence
def func_cap_sent():
    sentences = func_replac.split('.')
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


print(func_cap_sent())
n = func_cap_sent()


# This function will trigger script that will find all words that are followed by '.'
def func_findall():
    test1 = (re.findall(p, q))
    return test1


p = r'\w+\.'
q = func_cap_sent()
print(func_findall())


# This script will change our list back into string
def func_conv():
    test2 = ' '.join(func_findall())
    return test2


print(func_conv())
# Now we can replace '.' with spaces and capitalize again using functions created earlier.
b = func_conv()
l = '. '
m = ' '
func_replac = func_replace_param(b, l, m)
print(func_replac)

func_capitaliz = func_capitalize_param(func_replac)
print(func_capitaliz)


# Now we can join main text and our last sentence using another function.
def func_join1(k, m):
    final_text2 = k + ' ' + m
    return final_text2


k = str(n)
m = str(func_capitaliz)
o = func_join1(k, m)
print(o)


# Also need to replace capital letter for 'this', we can use the same function func_replace_param:
b = o
l = "  this"
m = "  This"
func_replac = func_replace_param(b, l, m)
print(func_replac)


# We can use unicode symbol of whitespace to find all of them in the text. We will use existing function 'func_findall'
p = '\s'
q = func_replac
print(func_findall())


# Now we calculate count of all found whitespaces using 'len':
def func_count():
    testcount1 = len(func_findall())
    return testcount1


print(func_count())








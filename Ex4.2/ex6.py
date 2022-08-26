# Example 1
name = 'Hello'
surname = 'Greygor'
print(f'{name} {surname}')

#  Example 2
name = "Hello Greygor"
(f'Hello, {name}!')
print(name)

#
def sentenceCapitalizer (string1: str):
    sentences = string1.split(". ")
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = '. '.join(sentences2)
    return string2
    print (sentenceCapitalizer("Today is not caps lock day"))

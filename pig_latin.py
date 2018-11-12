p = "Input a string to be Translated into pig latin:\n"
original=raw_input(p)

tokenised = original.split(' ')

out = ""

for words in tokenised:
    translated = words[1:(len(original))] + words[0]+"ay"

    if words[0].isupper():
        translated = translated.lower().capitalize()
        
    out += translated + ' '
    
print(out)

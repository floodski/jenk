p = "Input a string to be Translated into pig latin:\n"
original=raw_input(p)

translated = original[1:(len(original))] + original[0]+"ay"

if original[0].isupper():
    translated = translated.lower().capitalize()

print(translated)

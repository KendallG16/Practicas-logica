latter_list = {
    "a": "Д",
    "b": "ß",
    "c": "<",
    "d": "I>",
    "e": "[-",
    "f": "ƒ",
    "g": "gee",
    "h": "]-[",
    "i": "eye",
    "j": ",_]",
    "k": "|{",
    "l": "£",
    "m": "[]V[]",
    "n": "ท",
    "o": "Ø",
    "p": "[]D",
    "q": "0_",
    "r": "/2",
    "s": "ehs",
    "t": "†",
    "u": "บ",
    "v": "|/",
    "w": "(n)",
    "x": "Ж",
    "y": "¥",
    "z": "2"
}
word = input("Ingrese una palabra: ")
word = word.lower()
for i in word:
    if i in latter_list:
        word = word.replace(i, latter_list[i])
print(word)
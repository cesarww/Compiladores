estado = 'A'
text = ["VARIABLE", "ENTERO", "DECIMAL"]

for word in text:
    for l in word:
        if estado == "A":
            if l.isalpha() and 'A' <= l <= 'Z':
                estado = "A"
                print(estado)
            else:
                estado = "Z"
                print(estado)
                break
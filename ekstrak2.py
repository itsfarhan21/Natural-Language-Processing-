file = open('teks_artikel.txt', "r")
artikel = file.readlines()
print(artikel)

print(artikel, sep=".", end="\n")
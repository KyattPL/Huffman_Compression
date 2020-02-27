def huffman_decode(text, table):
    res = ""
    while text:
        for (k,val) in table.items():
            if text.startswith(val):
                res += k
                text = text[len(val):]
    return res

print("Podaj sciezke pliku do odkodowania:\n")
path = input()

with open(path, "r", encoding="utf-8-sig") as file:
    line = file.read()
    
with open("frequency", "r", encoding="utf-8-sig") as file:
    freq_table = file.read().splitlines()

huffman_encoding = dict()
for freq in freq_table:
    if freq[0] == " ":
        krotka = (" ", freq[2:])
        huffman_encoding[krotka[0]] = krotka[1]
    elif freq[0:2] == (r"\n"):
        value = freq.split()[1]
        huffman_encoding['\n'] = value
    else:
        krotka = freq.split()
        huffman_encoding[krotka[0]] = krotka[1]

converted_text = huffman_decode(line, huffman_encoding)
with open("decoded_file.txt", "w", encoding="utf-8-sig") as file:
    file.write(converted_text)

#siemandero elo bencka
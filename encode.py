def huffman_encode(text, table):
    res = ""
    for char in text:
        res += table[char]
    return res

def to_bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b)

print("Podaj sciezke pliku do zakodowania:\n")
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

converted_text = huffman_encode(line, huffman_encoding)
with open("converted_file.txt", "w", encoding="utf-8-sig") as file:
        file.write(to_bytes(converted_text))
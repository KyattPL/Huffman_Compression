def get_second(x):
    return x[1]

def sort_list(freq):
    return sorted(freq, key=get_second)

def huffman_decode(text, table):
    res = ""
    while text:
        for (k,val) in table.items():
            if text.startswith(val):
                res += k
                text = text[len(val):]
    return res

def huffman_encode(text, table):
    res = ""
    for char in text:
        res += table[char]
    return res

print("Podaj sciezke: (np. 'tadek.txt')\n")
path = input()

with open(path, "r", encoding="utf-8") as file:
    line = file.read()

frequency = list()
letters = set(line)

for index, letter in enumerate(letters):
    occurance = line.count(letter)
    frequency.append((letter, occurance))

sorted_frequency = sorted(frequency, key=get_second)
huffman_encoding = dict()

for (key,value) in sorted_frequency:
    huffman_encoding[key] = ""

while len(sorted_frequency) > 1:
    new_node = (sorted_frequency[0][0] + sorted_frequency[1][0],
                    sorted_frequency[0][1] + sorted_frequency[1][1])

    for char in sorted_frequency[0][0]:
        huffman_encoding[char] = "0" + huffman_encoding[char]

    for char in sorted_frequency[1][0]:
        huffman_encoding[char] = "1" + huffman_encoding[char]

    sorted_frequency.pop(1)
    sorted_frequency.pop(0)
    sorted_frequency.append(new_node)
    sorted_frequency = sort_list(sorted_frequency)

huffman_bits = 0

for item in frequency:
    char = item[0]
    huffman_bits += item[1]*len(huffman_encoding[char])

huffman_bytes = huffman_bits/8

print(len(line.encode()))
print(huffman_bytes)

x = input()

if x == "decode":
    with open("converted_file.txt", "r", encoding="utf-8") as file:
        line = file.read()
    converted_text = huffman_decode(line, huffman_encoding)
    with open("decoded_file.txt", "w", encoding="utf-8") as file:
        file.write(converted_text)
elif x == "encode":
    converted_text = huffman_encode(line, huffman_encoding)
    with open("converted_file.txt", "w", encoding="utf-8") as file:
        file.write(converted_text)
else:
    None
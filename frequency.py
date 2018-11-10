def get_second(x):
    return x[1]

def sort_list(freq):
    return sorted(freq, key=get_second)

print("Podaj sciezke: (np. 'tadek.txt')\n")
path = input()

with open(path, "r", encoding="utf-8-sig") as file:
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

with open("frequency", "w", encoding="utf-8-sig") as file:
    for (k, val) in huffman_encoding.items():
        if k != "\n":
            file.write(k + " " + val + "\n")
        else:
            string = "\\" + "n " + val + "\n"
            file.write(string)
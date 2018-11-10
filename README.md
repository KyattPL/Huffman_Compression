# Huffman Compression / Huffman Coding

This is a simple program that compresses your text file using the Huffman Compression method. Currently, the algorithm is split up to 3 different files. The whole project is written in Python.

Usage:
1. Firstly, run "python frequency.py" and then type the relative or absoulte path of your file (for which you'd like to make a frequency table of occurance for each possible value of the source symbol). This will automatically generate the "frequency" file (no extension!)
2. Next, run "python encode.py" and provide it with the relative or absolute path of your file (which you'd like to encode using the frequency table located in the "frequency" file).
3. Lastly, run "python decode.py" and provide it with the relative or the absolute path of your file (which you'd like to decode using the frequency table located in the "frequency" file).

Note:
Of course, you can use the generated frequency table to encode/decode any file (Compression ratio may and even certainly will differ). If your file contains any characters that don't appear in the frequency table, the program will fail.

"tadek.txt" and "idiota.txt" are polish poems, you can use them to test how the whole program is working!

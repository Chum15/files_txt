import os

filenames = ['text__2.txt','text_2.txt','text__1.txt', 'text_1.txt', 'text__3.txt', 'text_3.txt']
with open('nev_text.txt', 'w', encoding='UTF-8') as outfile:
    for fname in filenames:
        with open(fname, 'r', encoding='utf=8') as infile:
            for line in infile:
                outfile.write(line)

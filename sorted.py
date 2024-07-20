import os
# Вариант 1:
with open('text__1.txt', 'w')  as f:
    f = f.write('text_1.txt\n8\n')


with open('text__2.txt', 'w') as f:
    f = f.write('text_2.txt\n1\n')


with open('text__3.txt', 'w') as f:
   f = f.write('text_3.txt\n9\n')


filenames = ['text__2.txt','text_2.txt','text__1.txt', 'text_1.txt', 'text__3.txt', 'text_3.txt']
with open('nev_text.txt', 'w', encoding='UTF-8') as outfile:
    for fname in filenames:
        with open(fname, 'r', encoding='utf=8') as infile:
            for line in infile:
                outfile.write(line)



# Вариант второй:
with open('text__1.txt', 'w')  as f:
    f = f.write('text_1.txt\n8\n')


with open('text__2.txt', 'w') as f:
    f = f.write('text_2.txt\n1\n')


with open('text__3.txt', 'w') as f:
   f = f.write('text_3.txt\n9\n')

with open('new_text_2.txt','w', encoding='utf-8') as w:
    with open('text__2.txt','r') as r:
        w.write(r.read())

    with open('text_2.txt','r', encoding='utf-8') as r:
        w.write(r.read()) 

    with open('text__1.txt','r') as r:
        w.write(r.read())

    with open('text_1.txt','r', encoding='utf-8') as r:
        w.write(r.read())

    with open('text__3.txt','r') as r:
        w.write(r.read())

    with open('text_3.txt','r', encoding='utf=8') as r:
        w.write(r.read()) 

# Если снова не так, то я вообще не понимаю что требуется.          

import os.path

def comparator(doc):
    return len(doc[2])
 
def sorted_files():
    file_path = os.path.join(os.getcwd())
    file_list = []
    for root, dirs, files in os.walk(file_path):
        for name in files:
            if name.endswith(".txt"):
                with open(name, 'r',encoding='utf-8') as f:
                    f_1 =f.read()
                    f_2 = f_1.split('\n')
                    f_3 = str(len(f_2))
                    file_list.append([name, f_3, f_2])
                file_list.sort(key=comparator)
                
                with open('new_file', 'w', encoding='utf-8') as fi:
                    for filess in file_list:
                        fi.write(filess[0])
                        fi.write('\n')
                        fi.write(filess[1])
                        fi.write('\n')
                        fi.write('\n'.join(filess[2]))
                        fi.write('\n')

sorted_files()   
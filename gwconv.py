import os
import sys


first_name = "gb4n"
second_name = "gb4"
decode_name = "cp1251"
encode_name = "utf-8"

# if config is clear
main_name = "Genbase"
res_name = "Genbase6"
path4 = "geneweb-4.10/gw"
path6 = "geneweb-6.08/gw"

def load_cfg():
    fin = open("config.txt", "r")
    for line in fin.readlines():
        a, b = line.split('=')
        print(a, b)
        globals()[a.strip().rstrip()] = '/'.join(b.strip().rstrip().split('\\'))
    fin.close()

def recode():
    fin = open(path4 + "/" + first_name + ".gw", "rb")
    fout = open(path6 + "/" + second_name + ".gw", "wb")
    
    fout.write(("encoding: " + encode_name + "\n\n").encode(encode_name))
    
    for bline in fin.readlines():
        line = bline.decode(decode_name)
        for c in line:
            if ord('а') <= ord(c) <= ord('я') or ord('А') <= ord(c) <= ord('Я'):
                try:
                    fout.write(c.encode(encode_name))
                except Exception:
                    print(c)
                    raise
            else:
                fout.write(c.encode(encode_name))
                
    fin.close()
    fout.close()

def main():
    load_cfg()
    
    # create .gw file using gwu.exe from main base
    os.system('cd "' + path4 + '" & gwu.exe ' + main_name + ' -o ' + first_name + '.gw > comm.log')
    
    # create new .gw file with new encoding
    recode()
    
    # using new .gw file create new base ver6
    os.system('cd "' + path6 + '" & gwc.exe -nofail -f ' + second_name + '.gw -o ' + res_name + ' -nc > comm.log')


if __name__ == "__main__":
    main()
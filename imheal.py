import urllib.request
import os
import shutil

from tools import ru2en


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

def parse_name(s):
    sp = s.split('.')
    spp = sp[-1].split()
    return sp[0], spp[0], ' '.join(spp[1:])

def parse_url(url):
    for bline in urllib.request.urlopen(url).readlines():
        line = bline.decode("cp1251")
        sp = line.split("Изменить:<br>")
        if len(sp) > 1:
            s = sp[-1].split("</font>")[0]
            name, oc, surname = parse_name(s)
            return ru2en(name + "." + oc + "." + surname)
    return None

def main():
    load_cfg()
    
    # start gwd.exe from base4
    os.system('taskkill /f /im gwd.exe')
    os.system('cd "' + path4 + '" & start gwd.exe')
    
    for old_name in os.listdir(path4 + "/images/" + main_name):
        url_name = "%D7".join(old_name.split('Ч'))
        url_name = "%F7".join(url_name.split('ч'))
        
        try:
            name, oc, surname, _ = url_name.split('.')
        except Exception as e:
            print(e)
            print(url_name)
            continue
        
        url = "http://127.0.0.1:2317/" + main_name + "?lang=ru;m=U;p=" + name + ";n=" + surname + ";oc=" + oc
        try:
            new_name = parse_url(url)
        except Exception as e:
            print(e)
            print(url)
            break
        
        if new_name is None:
            print("parse_url error")
            print(url)
            continue
        
        if not os.path.exists(path6 + "/images/Genbase6/" + new_name + ".jpg"):
            if not os.path.exists(path6 + "/images/Genbase6"):
                os.makedirs(path6 + "/images/Genbase6")
            shutil.copyfile(path4 + "/images/Genbase/" + old_name, path6 + "/images/Genbase6/" + new_name + ".jpg")
    
    os.system('taskkill /f /im gwd.exe')

if __name__ == "__main__":
    main()
#Hesap Makinesi#
import time
import random
print("--------------Hesap Makinesi--------------")
time.sleep(3)
print("\n \n \n")
while True:
    log = open("hesapmakinesilog.txt" ,"a")

    print("İlk sayıyı girin")
    ilks = input(">>>")
    
    print("İşlemi girin")
    işlem = input(">>>")
        
    print("2. sayıyı girin")
    ikins = input(">>>")
    
   
    time.sleep(3)
    if işlem == "/":
        sonuç = float(ilks) / float(ikins)
    elif işlem == "*":
        sonuç = float(ilks) * float(ikins)
    elif işlem == "-":
        sonuç = float(ilks) - float(ikins)
    elif işlem == "+":
        sonuç = float(ilks) + float(ikins)
    else:
        print("Doğru düzgün bir İşlem yazmamışsın")
        exit()
    print("Sonuç")
    print(sonuç)
    log.write(ilks)
    log.write(işlem)
    log.write(ikins)
    log.write("=")
    log.write(str(sonuç))
    log.write("\n------------------\n")
    log.close()
    print("\n")
    time.sleep(5)
    

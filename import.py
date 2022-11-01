import time


tanlov = input("soz kriting: ")

if tanlov == 4444:
    print("togri: ")
else:
    a = 0
    print("siz xato malumot kritingiz: ")
    while a < 60:
        a += 1
        time.sleep(1)
        print(a)
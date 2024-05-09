import os
import time
PR=4500
OR=5000
PVR=5200
AER=4800
TPR=0
TOR=0
TPVR=0
TAER=0
pikaroll=0
otaroll=0
pulroll=0
anguiroll=0
desc=0

os.system("cls")

print("****Bienvenido****")
print("1. Pedir")
print("2. Salir")
hola=int(input("Igrese la opcion: "))

while hola==1:

    time.sleep(2)
    os.system("cls")

    print("******Menu******")
    print("1. Pikachu Roll $4500 ")
    print("2. Otaku Roll $5000 ")
    print("3. Pulpo Venenoso Roll $5200 ")
    print("4. Anguila Eléctrica Roll $4800 ")
    print("5. Salir")
    shushi=int(input("Ingrese la opcion: "))

    try:
        if shushi==1:
            pikaroll=int(input("Ingrese cuantos queire: "))
            TPR=(PR*pikaroll)
        elif shushi==2:
            otaroll=int(input("Ingrese cuantos queire: "))
            TOR=(OR*otaroll)
        elif shushi==3:
            pulroll=int(input("Ingrese cuantos queire: "))
            TPVR=(PVR*pulroll)
        elif shushi==4:
            anguiroll=int(input("Ingrese cuantos queire: "))
            TAER=(AER*anguiroll)
    except ValueError:
        break
  
    time.sleep(2)
    os.system("cls")

    print("1. pedir algo mas")
    print("2. salir")
    print("3. boleta")
    hola=int(input("Igrese la opcion: "))

totalpro=(pikaroll+otaroll+pulroll+anguiroll)
subttal=(TPR+TOR+TPVR+TAER)
if hola==3:
    time.sleep(2)
    os.system("cls")
    codigo=input("Ingreses codigo de decuento: ")

    if codigo=="soyotaku":
        descuento=((TPR+TOR+TPVR+TAER)/10)
        ta=((TPR+TOR+TPVR+TAER)-descuento)
        time.sleep(1)
        os.system("cls")
        print("****************************************")
        print(f"TOTAL PRODUCTOS: {totalpro}")
        print("****************************************")
        print(f"Pikachu Roll : {pikaroll}")
        print(f"Otaku Roll : {otaroll}")
        print(f"Pulpo Venenoso Roll: {pulroll}")
        print(f"Anguila Eléctrica Roll: {anguiroll}")
        print("****************************************")
        print(f"Subtotal por pagar: ${subttal}")
        print(f"Descuento por codigo: ${descuento}")
        print(f"TOTAL: ${ta}")
    else:
        time.sleep(1)
        os.system("cls")
        print("****************************************")
        print(f"TOTAL PRODUCTOS: {totalpro}")
        print("****************************************")
        print(f"Pikachu Roll : {pikaroll}")
        print(f"Otaku Roll : {otaroll}")
        print(f"Pulpo Venenoso Roll: {pulroll}")
        print(f"Anguila Eléctrica Roll: {anguiroll}")
        print("****************************************")
        print(f"Subtotal por pagar: ${subttal}")
        print(f"Descuento por codigo: ${desc}")
        print(f"TOTAL: ${subttal}")

time.sleep(20)
os.system("cls")
print("Volver a pedir")
print("1. SI")
print("2. NO")
hola=int(input("Igrese la opcion: "))
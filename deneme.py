import math
import random

print("-Nettin dünyalı ?" + "\n+İyi bea napak devrem sen naabüyün ? \n");

hafta = 14;
haftalıkDersSaati = 3;
toplam = hafta * haftalıkDersSaati;
print("toplam :" , toplam);

ağa = 5.6
print(type(ağa))  #float
print(int(ağa)) # 5
print(round(5.5)) # 6 integer
print(round(3.141592, 2)) # 3.14 float
print(round(3.141592, 0)) # 3.0 float
print(round(3113.14, -2)) # 3.100.0 float
print(float(12)) # 12.0

#abc = input("Bi sayı gir laa : ");
print(12 // 5) # 2  // bölümü verir
print(5 ** 2) # 25  // üssünü alır
print(5 * "M") # MMMMM
print(type(5==5)) #bool
print(5<6 or (7 < 7 or 8<8) and 5==4) #True it uses shortcut, 5<6 true and there is an "or" so whole is true
print((5<6 or (7 < 7 or 8<8)) and 5==4) #False it cannot use shortcut in this situation for a wrong answer

x = 13;
if x%2 == 0:
    print(x, "is an even number !")
elif x == 13:
    print(x, "is my favourite number !")
else :
    print("God sake ! What kind of number this(" + str(x) + ") is ?")

#These are not the same, the first thing that
print(12.2-12.1) #0.09999999999999964
print(0.2-0.1) #0.1

x=-13
print("|", x, "| = ", (-x if x<0 else x), sep="") #koşullu ifade

print(not False)

#for döngüsü
for i in range(1,11,2):
    a = 11-i
    #formatlı print
    print(("{0:3}{1:" + str(a) + "}{2:" + str(i) + "}").format(i, "."*a, 10**i))

kelime="kelime"
for harf in kelime:
    print(harf)

kelime = "ABC"
for ilk in kelime:
    for ikinci in kelime:
        if ilk != ikinci:
            for üçüncü in kelime:
                if üçüncü != ilk and üçüncü != ikinci:
                    #continue
                    mahmut=5
                    print(ilk + ikinci + üçüncü)

print(mahmut, "\n") #scope rules ?


boundary=13
counter=1
while counter <= boundary:
    print(" " * (boundary - counter) + "*" * (counter * 2 - 1))
    counter += 1

print("\n")

for ctr in range(1, boundary+1):
    print(" " * (boundary - ctr) + "*" * (ctr * 2 - 1))


abc = math.sqrt(4); # || from math import sqrt --> sqrt(4) || from math import * --> sqrt(4)

abc = round(random.random() * 15)
print(random.random() * 10)

print(random.randrange(0,2)) #returns a random number between [0, 2) 2 is not included
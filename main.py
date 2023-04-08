import sys

x = 0
kitaplar = []
raflar = []
z = 1
k = 0
rafSay = 0


bps = int(input("Raf başına kaç kitap konulsun? "))
i = "a"
while i != "exit":
    i = str(input("Kitap ismi: "))
    kitaplar.append(i)

sayilar = []
sayilar.extend(range((len(kitaplar))))
kitaplar.remove("exit")
kitaplar.sort()
kitaps = len(kitaplar)
for i in range(15):
    print("|")
print("v")

if bps >= kitaps:
    rafSay = 1
elif bps < kitaps:
    raf = kitaps % bps
    if raf == 0:
        rafSay = kitaps / bps
    else:
        rafSay = kitaps / bps + 1
try:
    
    for k in range(int(rafSay)):
        print("Raf " + str(z) + ":")
        for f in range(bps):

            print(kitaplar[0])

            x += 1
            if kitaps == 0:
                sys.exit()
            else:
                kitaplar.remove(kitaplar[0])

        z += 1
        if kitaps == 0:
            sys.exit()
except:
    sys.exit()

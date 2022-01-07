sonlar = []
for i in range(10)
    son = int(input(f"{i+1}-sonni kiriting:"))
    sonlar.append(son)
print(sonlar)
beshga_bolinadiganlar = []
for i in sonlar:
    if i%5 == 0:
        beshga_bolinaduganlar.append(i)
print(f"Bular 5ga qoldiqsiz bolinadi:{beshga_bolinadiagnalar}")

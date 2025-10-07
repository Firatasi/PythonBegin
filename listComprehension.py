sayilar = [18, 22, 5, 3, 43, 25]
yeni_sayilar = [sayi * 2 for sayi in sayilar]
print(yeni_sayilar)

#uzun hali
dene = []
for sayi in sayilar:
    dene.append(sayi * 2)
print(dene)


plakalar = [1, 6, 34, 35, 41, 67]
yeni_plakalar = [plaka ** 10 for plaka in plakalar]
print(yeni_plakalar)


listem = [characters for char in ["Python", "Java", "C#", "JavaScript"] for characters in char]
print(listem)

#çift sayılar
cift_sayilar = [sayi for sayi in range(1, 101) if sayi % 2 == 0]
print(cift_sayilar)


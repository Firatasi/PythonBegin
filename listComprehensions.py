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

numbers = [-1, -2, 0, 1, 2]
pozitif_sayilar = [num for num in numbers if num > 0]
print(pozitif_sayilar)

yy = ["çift sayi" if num % 2 == 0 else "tek sayi" for num in range(8)]
print(yy)

sicakliklar = [10, 20, 30, 40, 50]
farenheit = [((9/5) * derece + 32) for derece in sicakliklar]
print(farenheit)

words = ["hello", "world", "python", "is", "awesome"]
modified_words = [word if len(word)>3 else "kısa kelime" for word in words]
print(modified_words)

notlar = [55, 70, 85, 100, 90]
harf_notlari = ["A" if not_ >= 90 else "B" if not_ >= 80 else "C" if not_ >= 55 else "D" for not_ in notlar]
print(harf_notlari)

names = ["Ali", "Veli", "Ayşe", "Fatma","Firat"]
greetings = ["A" + name[1:] if name[0]=="A" else "B" + name[1:] for name in names]
print(greetings)

#list comprehensions with functions

def digitSum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

list1 = [123, 456, 789]
list2 = [digitSum(num) for num in list1 if num%2 != 0]
print(list2)

matris = [  [j for j in range(3)] for i in range(5)]
print(matris)

isim = "FIRAT"
listem = [chr for chr in isim] #her karakteri listeye atar  
print(listem)


#lambda functions with list comprehensions
x = lambda a: a * 2 #tek parametreli a yerine a*2 döner a yerine 5 geliyorsa 10 döner
print(x(5))

y = lambda a,b: a+b #iki parametreli a ve b toplanır
print(y(3,5))

z = lambda a,b,c: a*b*c #üç parametreli a,b,c çarpılır
print(z(2,3,4)) 

def math(n):
    return lambda a: a * n #n parametresi dışarıdan alınır a parametresi fonksiyon çağrılırken alınır
doubler = math(2) #n=2 olur
print(doubler(11)) #a=11 olur 2*11=22 döner

tripler = math(3) #n=3 olur
print(tripler(11)) #a=11 olur 3*11=33 döner

even_numbers = [2,4,6,8,10]
squared_numbers = [(lambda x: x**2) (i) for i in even_numbers] #her elemanı karesini alır
print(squared_numbers) 

words = ["hello", "world", "python","ha"]
word_length = [word + "kelimesi dırejdır" if len(word) > 3 else word + "kelimesi kındır" for word in words]
print(word_length)


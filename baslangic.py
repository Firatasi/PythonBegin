#variables (değişkenler)
x=5
y="John"
print(x)
print(y)

#casting
x=3
print(type(x))   #type demek ne classı olduğu
x= str(3)  #int sayıyı stringe döndürür
y=int(3) 
z=float(3)
print(type(x))
print(x)
print(y)
print(z)
x="ali" 
y='ali'
z="""adamsın la sen gardaş"""
print(z)
#case sensivite
a=4
A="john"
print(a)
print(A)
#many values to multiple variables
x,y,z="elma","armut","vişne"
print(x)
print(y)
print(z)
#one value to multiple variables
x=y=z="ayva"
print(x)
print(y)
print(z)

#unpack a collection
fruits=["elma","muz","vişne"]
x,y,z=fruits
print(x)
print(y)
print(z)

#global variables
x=" ve tektir"
def myfunc():
    print("allah var la gardaş"+x)
myfunc()    
x="dünya"
def myfunc():
    x=" şarkı yaptı ülkeyi salladı"
    print("baba"+x)
myfunc()
print("baba "+x)    
#global keyword
def myfunc():
    global x
    x="lvbelc5"
myfunc()
print("ülkenin en iyi rapçisi baba globali olan adam= "+x)

#global devam
x="dünya hain"
def myfunc():
    global x
    x="tak tak tak"
myfunc()
print("ülkenin en iyi şarkısı = "+x)
#data types
x="hello worlds"
print(type(x))
x=20
print(type(x))
x=1j
print(type(x))
x=20.5
print(type(x))
x=["elma","armut","kayısı"]
print(type(x))
x=("elma","armut","kayısı")
print(type(x))
x=range(6) #0 ile 6 arası sayı üretmek
print(type(x))
x={"elma","armut","kayısı"}
print(type(x))
x={"name":"watson","age":34}
print(type(x))
#list set tuples
mylist=[1,2,2,3]
mylist[0]=100
print(mylist)
mylist.append(4)
print(mylist)
#tuple
mytuple=(1,2,2,3)
print(mytuple)
mytuple(0)=100 #tuple sonradan elemanları değişemez hata alırız
print(mytuple)

#set
myset={1,2,3} #her elemeandan bir tane yazdırılır o yüzden yine 1 2 3 yazdırır
print(myset)
myset={1,2,2,3}
print(myset)
myset.add(9) #add ya da remove yapılabilir
myset[0]=100 #yine izin verilmez değişim yapılamaz
print(myset)

#string arrayler
a="hello world"
print(a[0])

#h harfini verir bunlarda bi array yani kanki

print(len(a))

for x in "mehmet akif ersoy":
   # print(x)
    print(x,end=" ")
#check string
txt="bilişim sistemleri mühendisliğinde okuyorum"
print("makü"in txt)
print("bilişim"in txt) #var mı diye kontrol ediyor

#slicing 
txt="hello world"
print(txt[1:4]) #1.indeksten 4.indekse kadar ama 4.indesk hariç

print(txt[:5]) #0.indeksten 5.indekse kadar ama 5.indesk hariç
print(txt[3:]) #3.indeksten sona kadar git
print(txt[-4:-2]) #geriden bu da
#modify string
a="   helLO world     "
print(a.upper())
print(a.lower())
print(a.strip())#gereksiz boşluklar temizlenir
print(a.replace("h","j"))
print(a.split(" "))
#string concatenation
a="hello"
b=" world"
c= a+b
print(c)
#string format

age=36
txt="my name is john ,I am "+str(age)  #string değer ile int değer toplanmaz
print(txt)

#F-string
age=45
txt=f"my name is john ,I am {age} years old"#string değer ile int değer toplanmaz
print(txt)

#string methods devam
txt="hello,and come welcome to my world"
x=txt.capitalize()
print(x)

x=txt.endswith(".")
print(x)

txt="companyX123"
x=txt.isalpha() #sadece harf mi diye soruyo
print(x)

txt="50"
x=txt.zfill(10) #başına 10 tane sıfır ekler
print(x)
print(10>9)
print(10==9)
print(10<9)

#operetors devam
#basit hesap makinesi 3.Hfta **************************************************

a = int(input("ilk sayıyı giriniz: "))
b = int(input("ikinci sayıyı giriniz: "))

print("toplama işlemi sonucu: ",a+b)
print("çıkarma işlemi sonucu: ",a-b)    
print("çarpma işlemi sonucu: ",a*b)
print("bölme işlemi sonucu: ",a/b)
print("mod alma işlemi sonucu: ",a%b)
print("üs alma işlemi sonucu: ",a**b)   
print("bölümden kalma işlemi sonucu: ",a//b)

#karşılaştırma operatörleri
print("a==b: ",a==b)
print("a!=b: ",a!=b) 
print("a>: ",a>b)
print("a<b: ",a<b)
print("a>=b: ",a>=b)
print("a<=b: ",a<=b)

#python list
thisList=["elma","armut","muz"]
print(thisList)
print("Dizi uzunluğu: ",len(thisList))
print(thisList[0])
print(thisList[-1]) #son elemanı verir
thisList[0]="çilek" #ilk elemanı çilek yapar
print(thisList)
thisList=["elma","karpuz","armut","ayva","su aygırı"] 
print("son hali: ",thisList) 

#append
thisList.append("mandalina") #sona ekler
print("append sonrası: ",thisList)

#insert
thisList.insert(1,"kivi") #1.indekse kivi ekler 
print("insert sonrası: ",thisList)

#remove
thisList.remove("armut") #armutu siler
print("remove sonrası: ",thisList)

#pop
thisList.pop() #son elemanı siler   
print("pop sonrası: ",thisList)

thisList.pop(1) #1.indeksteki elemanı siler
print("pop 1 sonrası: ",thisList)

#extend
tropical=["ananas","mango"]
thisList.extend(tropical) #iki listeyi birleştirir

#remove del clear
thisList.remove("elma") #elmayı siler
thisList.clear() #tüm listeyi siler
print("clear sonrası: ",thisList)

#del thisList #listeyi komple siler
del thisList


#while loop
thisList=["elma","karpuz","armut","ayva","su aygırı"] 
i=0
while i<len(thisList):
    print(thisList[i])
    i+=1    

#tek satırda döngü
thisList=["elma","karpuz","armut","ayva","su aygırı"]
[x for x in thisList] #list comprehension
print(thisList, end=" ")

#sort list
thisList=["elma","karpuz","armut","ayva","su aygırı"]
thisList.sort() #alfabetik sıralar
print(thisList)
thisList.sort(reverse=True) #ters alfabetik sıralar
print(thisList) 

#copy list
thisList=["elma","karpuz","armut","ayva","su aygırı"]   
mylist=thisList.copy() #kopyalama
print(mylist, end=" ")

#remove item from list
thisList=["elma","karpuz","armut","ayva","su aygırı"]
thisList.remove("armut") #değer ile siler
print(thisList)

thisList.pop(1) #indeks ile siler
print(thisList)

del thisList[0] #indeks ile siler
print(thisList)

thisList.clear() #tüm listeyi siler
print(thisList)

del thisList #listeyi komple siler
#print(thisList) #hata verir çünkü liste silindi

#Dictionary
thisList={
    "brand":"Ford",
    "model":"mustang",
    "year":1964
}

x =thisList["model"] #model değerini verir
print(x)

y=thisList.get("model") #model değerini verir
print(y)

x=thisList.keys() #tüm keyleri verir
print(x)

x=thisList.values() #tüm değerleri verir
print(x)

x=thisList.items() #key ve value çiftlerini verir
print(x)

thisdict= {
  "brand": "Ford",
  "model": "fiesta",
  "year": 1764}

thisdict.pop("model") #modeli siler
print(thisdict)

for x in thisdict:
    print(x) #keyleri yazdırır


for x in thisdict.keys():
    print(x) #keyleri yazdırır

for x in thisdict.values():
    print(x) #value değerlerini yazdırır

for x,y in thisdict.items():
    print(x,y) #key ve value çiftlerini yazdırır


a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#basit if else örneği

#while break
i=1 #1 den başla
while i<6: #6 dan küçük olduğu sürece
    print(i)
    if i==3: #i 3 e eşit olduğunda
        break #döngüyü kır
    i+=1 #i yi 1 artır


#while continue
i=0
while i<6:  
    i+=1
    if i==3:
        continue #3 ü atla
    print(i)



fruits=["elma","armut","muz"]
for x in fruits:
    print(x)
    if x=="armut":
        break #armut u görünce döngüyü kır

#functions
def my_function():
    print("hello from a function")  
my_function()


def my_function(fname,lname):
    print(fname + " " + lname)
my_function("emre","şahin")
my_function("ali","veli")

#arbitrary arguments
def my_function(*kids): #kaç tane argüman gelirse gelsin kabul eder
    print("the youngest child is " + kids[2]) #2.indeksi yazdırır   
my_function("emre","ali","veli")
my_function("ahmet","mehmet","ayşe","fatma")

def demo_function(*args): #key value şeklinde argüman alır
    if len(args) >= 3:
        print("2.index: ", args[2])
    elif len(args) == 2:
        print("1.index: ", args[1])
    else:
        print("Not enough arguments")   
    
demo_function("elma", "armut", "muz")
demo_function("elma", "armut")

#keyword arguments
def my_function(child3, child2, child1): #key value şeklinde argü
    print("the youngest child is " + child3) #2.indeksi yazdırır

my_function(child1 = "emre", child2 = "ali", child3 = "veli")


def my_function(**kwargs): #key value şeklinde argüman alır
    print("his last name is " + kwargs["lname"]) #2.indeksi yazdırır
    print("his first name is " + kwargs["fname"])#1.indeksi yazdırır
my_function(fname = "emre", lname = "şahin")
my_function(fname = "ali", lname = "veli")





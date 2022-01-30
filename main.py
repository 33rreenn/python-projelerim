#tamsayı = Integer / ondalıklı sayı = Fload

#Basit Matematik Operatörleri
print(33 + 33) #toplama
print(24 - 21) #çıkarma
print(11 * 11) #çarpma
print(12 / 2) #bölme

#________________________________________________________________

#Değişkenler ve Değişken Tanımlama


#değişken isimi & değişken değeri [NOT = DEĞİŞKEN DEĞERİ HERZAMAN SAYI OLMALIDIR]
eren = 10
print(eren)
# = 10
#peki biz bu eren değişkenini başka nerede kullana biliriz ?

#mesela
print(eren * eren)
# = 100


#mesela
é = 2
print((eren * eren)/é)
# = 50


#mesela
a = 9.44
b = 44
c = 58
print((a+b)*c)
#= 3099.52

#msl
a = 32
b = 12
c = a + b
print((c + a)/b)
#= 6.333333333333333

#HATLI KOD SSEBEBLERİ

# 1. Değişken isimleri bir sayı ile başlayamaz
# 2. Değişken isimi kelimelerden oluşuyorsa aralarında boşluk olmaz.
# 3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
# 4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )

# ör:

# 3ren = 100
# print(3ren)
#= HATA "1.kural

#MSL

# ?eren = 1
# print(?eren)
# = HATA "3. kural"

#msl
_eren_eren = 100
print(_eren_eren)
# = 100 [✓ DOĞRU HATASIZ ✓]"2.kural"

#msl
#while = 22
#print = while
#= HATA "4.kural"

#Bi dairenin çevresini hesaplama
pi_sayısı = 3.14
çap = 53
çevre = pi_sayısı * çap #ilk önce sağ daki değer hesaplanıyor sonra çevreye bu değer atanıyor
print(çevre)
# = 166.42000000000002

#Pythonda çok güzel bir özellik var , mesela sizin elinizde 2 tane değişken var a nın içinde 4 değeri var b nin içinde 8
#siz bunların değerlerini birbiriyle değiştirmek istiyor sanız ;

a = 4
b = 8
a,b = b,a #böylelikle a nın içindeki veri b nin b nin içindeki veri a nın içinde
print(a)#= 8
print(b)#= 4


p = 5 #mesela ben bu değişkenin değerini 2 artırmak istiyorum
p = p + 2
print(p)

#______________________________________________________________________________________________________________

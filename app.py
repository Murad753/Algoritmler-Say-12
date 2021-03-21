# 1. Ekrana istifadəçinin daxil etdiyi say qədər, ulduzlardan üfiqi xətt çıxaran proqram yazın.

# Method 1
'''user = int(input('Sayinizi Girin: '))

for x in range(user):
    x = '*'
    print(x, end='')'''

# Method 2
'''user = int(input('Sayinizi Girin: '))

for x in range(user):
    print('*', end='')'''

# 2. Ekrana, 1-50 aralığındakı rəqəmlərdən ancaq cüt olanları çıxaran proqram yazın.
# Method 1
'''user = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

for x in user:
    if x % 2 == 0:
        print(x)'''
# Method 2
'''for x in range(1,50):
    if(x % 2 == 0):
        print(x)
    '''

# Method 3
'''a = 0
while(a < 50):
    if(a % 2 == 0):
        print(a)
    a+=1'''
# 3. İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30) cüt rəqəmlərin cəmini tək rəqəmlərin hasilini hesablayan proqram yazın. 

# Method 1
'''user = int(input('Sayinizi Girin: '))
odd = 1
even = 0
for i in range(1,user):
    if (i % 2 == 0):
        even+=i
    elif (i % 2 == 1):
        odd *=i

print(f'Cut Saylarin Toplami {even}')
print(f'Tek Saylarin Hasili {odd}')'''
# 4. 1-100 diapazonunda 3-ə bölünüən bütün ədədləri ekrana çıxaran proqram yazın. 

# Method 1
'''for x in range(1,100):
    if (x % 3 == 0):
        print(x)'''

# Method 2
'''a = 0
while(a < 100):
    a+=1
    if (a % 3 == 0):
        print(a)'''


# 5. Ədədin faktorialını tapan proqram yazın. (Məsələn (! - faktorial işarəsidir), 5! = 1*2*3*4*5) 

'''user = int(input('Sayinizi Girin: '))

a = 1
while (user >= 1):
    a *= user
    user -= 1
print(a)'''

# 6. Ədədin üstünü hesablayan proqram yazın (istifadəçi iki ədəd daxil edəcək əsas və üst məs. 2 və 3 cavab 8 alınmalıdır) 

# Method 1
'''user = int(input('Sayinizi Girin: '))
user2 = int(input('Sayinizi Girin: '))

ust = user**user2
print(ust)'''

# Method 2
'''user = int(input('Sayinizi Girin: '))
user2 = int(input('Sayinizi Girin: '))

toplam = pow(user,user2)
print(toplam)'''

# 7. İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, onun rəqəmlərinin sayını və onların cəmini hesablayan proqram yazın.

'''user = int(input('Sayinzii Girin: '))
toplam = 0
say = 0

while (user > 0):
    toplam = toplam + (user % 10)
    say+=1
    user = user // 10

print(f'Girdiyiniz Ededin reqemlerinin sayi: {say}')
print(f'Girdiyiniz Ededin reqemlerinin toplami: {toplam}')'''


# 8. İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, ədədi əksinə çevirən proqram yazın.

'''user = int(input('Sayinizi Girin: '))

reverse_number = 0

while(user > 0):
    qaliq = user % 10
    reverse_number = (reverse_number * 10) + qaliq
    user = user // 10

print('Girdiyiniz ededin tersi: ', reverse_number)'''

 
# 9. İstifadəçi tam ədəd daxil edir, bu ədədin qalıqsız bölündüyü bütün rəqəmləri ekrana çıxaran proqram yazın.

# Method 1
'''user = int(input('Sayinizi Girin: '))
i = 2
for x in range(1,user+1):
    if (user % i == 0):
        print(i)
        user = user / i
    else:
        i += 1'''

# Method 2
'''user = int(input('Sayinizi Girin: '))
i = 2
while(user >= 0):
    if (user % i == 0):
        print(i)
        user = user / i
    else:
        i+= 1'''


# 10. İstifadəçi tam ədəd daxil edir , bu ədədin sadə olub olmamasını tapan proqram yazın.

# 11. Daxil edilmiş ədəddə iki ard arda rəqəmin olub olmamasını yoxlayan proqram yazın. 
# 12. İstifadəçi ədəd daxil edir, bu ədədin rəqəmlərinin artan ardıcıllıqla olub olmamasını yoxlayan proqram yazın. (12299 artan ardıcıllıq, 122044 artan ardıcıllıq deyil.

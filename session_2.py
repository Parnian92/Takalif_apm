#Homework1-Jalase 2

#1) reshteyi shamel name va melli code be ham chasbide az karbar begirid ba slicing bakhshe adadi ra joda karde va ba castbe int tabdil namayid.
data=input('enter name and melli code:')
melli_code=int(data[-10:])
print('melli code:',melli_code)

#2) shomare mobile 11 raghami az karbar begiri, ba slicing code operator ra joda karde o chap namayid.
mobile=input('enter mobile number:')
operator=mobile[1:4]
print('operator code:',operator)

#3) name kamel karbar ra begirid va ba indexing va slicing, khoruji barname ra be surat harf aval name va kole family name besazid.
full_name=input('enter your name and family name:')
first_name, last_name=full_name.split()
result=f'{first_name[0]}.{last_name}'
print('result:',result)



#4) shomare hesab banki az karbar begirid va ba slicing noskhe makus aan ra chap namayid.
account=input('enter account number:')
print(account[::-1])

#5) barnameyi benevisid masafat tey shode bar hasb km begirad.agar masafat kamtar az 2km bud keraye sabet 20000 toman bashad. dar gheyre in surat be ezaye har km ezafe, 5000 toman keraye ezafe shavad. keraye nahayi ra chap namayid.
distance=float(input('enter distance(km):'))
if distance<2:
    fare=20000
    print('final fare:',fare,'tooman')
else:
    fare=20000+(distance-2)*5000
    print('final fare:',fare,'tooman')
    
#6) barnameyi benevisid ke mablagh kharid az karbar begirad. agar balaye 1 million tooman bud 15% takhfif, beyne 500000 ta 1 million 10% takhfif va kamtar az an bedoon takhfif emal shavad. mablagh nahayi chap shavad.
price=int(input('enter the price:'))    
if price>1000000:
    final_price=price*0.85
    print('final price:',final_price,'tooman')
elif price>500000:
    final_price=price*0.9
    print('final price:',final_price,'tooman')
else:
    final_price=price
    print('final price:',final_price,'tooman')
    
#7) barnameyi benevisid ke shomare card 16 raghami az karbar daryaft konad.4 raghame aval ra joda konid va barresi konid ke aya ba yeki az pish shomarehaye banki moshakhas motabeghat darad ya na va name bank ra chap konid.
card=input('enter your card number:')
prefix=card[:4]
if prefix=='6037':
    print('Melli Bank')
else:
    print('unknown bank')
   
#8) saati beyne 0 ta 23 az karbar begirid va baze zamani rooz(sobh,zohr,asr,shab) ra tayin namayid.hamchenin agar adad kharej az baze motabar bud, payame khata chap namayad.
hour=int(input('enter the time(0-23):' ))
if 0<=hour<6:
    print('night')
elif 6<=hour<12:
    print('morning')
elif 12<=hour<17:
    print('noon')
elif 17<=hour<21:
    print('evining')
elif 21<=hour<=23:
    print('night')
else:
    print('the time is out of range')

    

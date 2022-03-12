import phonenumbers
from phonenumbers import geocoder


tel = input('Digite o Telefone no formato +5511945639875 :')

phone = phonenumbers.parse(tel)

print(geocoder.description_for_number(phone ,'pt'))

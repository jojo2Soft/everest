#first programme

name_user = input("Entrer votre nom ")
age_user = int(input("entrer votre age "))

while age_user <=0 or age_user >=100:
    print("Votre age doit etre strictement positif")
    age_user = int(input("entrer votre age "))
print("Bonjour ", name_user , " ", age_user ," ans")
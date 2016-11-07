class Contact(object):

    def __init__(self, first_name, last_name, phone_number, email, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.birth_year = int(birth_year)
        self.age = 2016 - self.birth_year

    def izpisi_kontakt(self):
        return self.last_name + ", " + self.first_name + ": " + str(self.phone_number)

    def starost_v_mesecih(self):
        return self.age * 12

moji_kontakti = []

def dodaj_kontakt():
    ime = raw_input("ime")
    priimek = raw_input("priimek")
    phone = raw_input("phone")
    email = raw_input("email")
    year = raw_input("year")

    kontakt = Contact(ime, priimek, phone, birth_year=year, email=email)

    moji_kontakti.append(kontakt)


def izberi_kontakt():
    
    
    num = int(raw_input("vpisi zaporedno stevilko kontakta"))
    
    if not ( 0 <= num < len(moji_kontakti)):
        print("Takega kontakta ni")
        return -1
    return num

def izbrisi_kontakt():
    num = izberi_kontakt()
    if num == -1:
        
        return
    
    print("Brisem ....")
    
    bliznjica = False
    if bliznjica:
        
        izbrisani = moji_kontakti.pop(num)
    else:
        
        izbrisani = moji_kontakti[num]
       
        del moji_kontakti[num]


    print("Izbrisal: " + izbrisani.izpisi_kontakt())

def uredi_kontakt():
    num = izberi_kontakt()
    if num == -1:
        
        return
  
    print("Urejanje: " + moji_kontakti[num].izpisi_kontakt())
    ime = raw_input("ime")
    priimek = raw_input("priimek")
    phone = raw_input("phone")
    email = raw_input("email")
    year = raw_input("year")

    
    kontakt = Contact(ime, priimek, phone, birth_year=year, email=email)

    
    moji_kontakti[num] = kontakt

    

def izpisi_kontakte():
    print("St \t| Kontakt")
    print("-"*50)
    for j in range(len(moji_kontakti)):
        print(str(j) + "\t| " + moji_kontakti[j].izpisi_kontakt())

while True:
    odgovor = raw_input("Povej kaj zelis narediti (dodaj, izbrisi, uredi, izpisi, koncaj)?").lower()
    
    if odgovor == "dodaj":
        dodaj_kontakt()
    elif odgovor == "uredi":
        uredi_kontakt()
    elif odgovor == "izbrisi":
        izbrisi_kontakt()
    elif odgovor == "izpisi":
        izpisi_kontakte()
    elif odgovor == "koncaj":
        break
    else:
        print("Nisem razumel odgvora :(")









with open("contact.txt", "w+") as contact_file:
    contact_file.write("Tvoji kontakti:\n")
    for kontakt in moji_kontakti:
        contact_file.write("-" + str(kontakt.first_name) + ";\t")
        contact_file.write(str(kontakt.last_name) + ";\t")
        contact_file.write(str(kontakt.phone_number) + ";\t")
        contact_file.write(str(kontakt.email) + ";\t")
        contact_file.write(str(kontakt.birth_year) + ";\n")
    









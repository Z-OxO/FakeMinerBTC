from random import *
from colorama import *
from time import *
from secrets import *
import os
import requests
from bs4 import BeautifulSoup
import base58
import hashlib
import binascii


just_fix_windows_console()
print(Style.RESET_ALL)


# banner variables
banner_text = '''
 ---------------------------------------------------------------------------   
╔══╗ ╔══╗╔════╗╔═══╗╔═══╗╔══╗╔═╗ ╔╗    ╔═╗╔═╗╔══╗╔═╗ ╔╗╔═══╗╔═══╗        ╔═══╗
║╔╗║ ╚╣╠╝║╔╗╔╗║║╔═╗║║╔═╗║╚╣╠╝║║╚╗║║    ║║╚╝║║╚╣╠╝║║╚╗║║║╔══╝║╔═╗║        ║╔═╗║
║╚╝╚╗ ║║ ╚╝║║╚╝║║ ╚╝║║ ║║ ║║ ║╔╗╚╝║    ║╔╗╔╗║ ║║ ║╔╗╚╝║║╚══╗║╚═╝║    ╔╗╔╗╚╝╔╝║
║╔═╗║ ║║   ║║  ║║ ╔╗║║ ║║ ║║ ║║╚╗║║    ║║║║║║ ║║ ║║╚╗║║║╔══╝║╔╗╔╝    ║╚╝║╔═╝╔╝
║╚═╝║╔╣╠╗ ╔╝╚╗ ║╚═╝║║╚═╝║╔╣╠╗║║ ║║║    ║║║║║║╔╣╠╗║║ ║║║║╚══╗║║║╚╗    ╚╗╔╝║║╚═╗
╚═══╝╚══╝ ╚══╝ ╚═══╝╚═══╝╚══╝╚╝ ╚═╝    ╚╝╚╝╚╝╚══╝╚╝ ╚═╝╚═══╝╚╝╚═╝     ╚╝ ╚═══╝ 
 ---------------------------------------------------------------------------  
 
'''

banner_verif1 = """
                 _                                                      _   _       _           _     _                       
     /\         | |                                                    | | (_)     | |         | |   (_)                      
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __        
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \       
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_)
                                                                                                                              
                                                                                                                              
 """

banner_verif2 = """
                 _                                                      _   _       _           _     _                           
     /\         | |                                                    | | (_)     | |         | |   (_)                          
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __            
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \           
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _   _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_) (_)
                                                                                                                                  
                                                                                                                                                                      
 """

banner_verif3 = """
                 _                                                      _   _       _           _     _                               
     /\         | |                                                    | | (_)     | |         | |   (_)                              
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __                
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \               
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _   _   _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_) (_) (_)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

 """

banner_mining1 = '''

   _____    ____    _   _   _   _   ______    _____   _______   _____    ____    _   _     
  / ____|  / __ \  | \ | | | \ | | |  ____|  / ____| |__   __| |_   _|  / __ \  | \ | |    
 | |      | |  | | |  \| | |  \| | | |__    | |         | |      | |   | |  | | |  \| |    
 | |      | |  | | | . ` | | . ` | |  __|   | |         | |      | |   | |  | | | . ` |    
 | |____  | |__| | | |\  | | |\  | | |____  | |____     | |     _| |_  | |__| | | |\  |  _ 
  \_____|  \____/  |_| \_| |_| \_| |______|  \_____|    |_|    |_____|  \____/  |_| \_| (_)
                                                                                           

'''
banner_mining2 = '''

   _____    ____    _   _   _   _   ______    _____   _______   _____    ____    _   _         
  / ____|  / __ \  | \ | | | \ | | |  ____|  / ____| |__   __| |_   _|  / __ \  | \ | |        
 | |      | |  | | |  \| | |  \| | | |__    | |         | |      | |   | |  | | |  \| |        
 | |      | |  | | | . ` | | . ` | |  __|   | |         | |      | |   | |  | | | . ` |        
 | |____  | |__| | | |\  | | |\  | | |____  | |____     | |     _| |_  | |__| | | |\  |  _   _ 
  \_____|  \____/  |_| \_| |_| \_| |______|  \_____|    |_|    |_____|  \____/  |_| \_| (_) (_)
                                                                                                                                                                             
                                                                                                                                                                             
'''
banner_mining3 = '''

   _____    ____    _   _   _   _   ______    _____   _______   _____    ____    _   _             
  / ____|  / __ \  | \ | | | \ | | |  ____|  / ____| |__   __| |_   _|  / __ \  | \ | |            
 | |      | |  | | |  \| | |  \| | | |__    | |         | |      | |   | |  | | |  \| |            
 | |      | |  | | | . ` | | . ` | |  __|   | |         | |      | |   | |  | | | . ` |            
 | |____  | |__| | | |\  | | |\  | | |____  | |____     | |     _| |_  | |__| | | |\  |  _   _   _ 
  \_____|  \____/  |_| \_| |_| \_| |______|  \_____|    |_|    |_____|  \____/  |_| \_| (_) (_) (_)
                                                                                                                                                                             
                                                                                                                                                                             
'''
banner_bank = '''
 ____                    _    
 |  _ \                  | |   
 | |_) |   __ _   _ __   | | __
 |  _ <   / _` | | '_ \  | |/ /
 | |_) | | (_| | | | | | |   < 
 |____/   \__,_| |_| |_| |_|\_|
                               
'''
x = randint(1, 1000)

#BTC live price
def Btc_live():
    global valeur_btc
    try:
        url = "https://coinmarketcap.com/fr/currencies/bitcoin/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        balise = soup.find('div', {'class': 'priceValue'})
        if balise is not None:
            # récupérer la valeur de la balise
            valeur = balise.text
            # afficher la valeur récupérée
            valeur_btc=""
            for caractere in valeur:
                if caractere.isdigit():
                    valeur_btc += caractere
            print(Fore.CYAN+"The BTC value is",valeur_btc,"$")
            return True
        else:
            print("Bitcoin price not found")
            return False
    except:
        print("Bitcoin price synchronization error")
        return False


# Menu de la vérification de l'adresse
def Decoder_menu():
    global adresse
    Fore.RESET
    adresse = input("Enter a bitcoin address (type 'end' to exit): ")
    if adresse == "end":
        exit("Program interrupted by user")
    for i in range(1, 12):
        loading(banner_verif1, banner_verif2, banner_verif3)
    sleep(4)
    Fore.RESET
    Decode(adresse)
    Menu()


# Vérification de l'adresse
def Decode(adresse):
    base58Decoder = base58.b58decode(adresse).hex()
    prefixAndHash = base58Decoder[:len(base58Decoder)-8]
    checksum = base58Decoder[len(base58Decoder)-8:]
    hash = prefixAndHash
    for x in range(1,3):
        hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    if (checksum == hash[:8]):
            print(Fore.GREEN+"BTC adress is valid !")
            sleep(3)
            Fore.RESET
            Menu()
    else:
        print(Fore.RED+"BTC adress is not valid !")
        Fore.RESET
        sleep(3)
        Decoder_menu()


Btc_live()

# Création du dossier "FakeMiner" s'il n'existe pas déjà
if not os.path.exists("FakeMiner"):
    os.makedirs("FakeMiner")

# Création du fichier "bank.txt" s'il n'existe pas déjà
filename = os.path.join("FakeMiner", "bank.txt")
if not os.path.exists(filename):
    with open(filename, "w") as fichier:
        fichier.write("Welcome in the bank")


def loading(image1, image2, image3):
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image1)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image2)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image3)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")


# Fonction de minage
def Miner():
    global valeur_btc
    global adresse
    for i in range(1, 9):
        loading(banner_mining1, banner_mining2, banner_mining3)
    while True:
        hex = ("0x" + str(token_hex(20)))  # Token en hex
        print(Fore.RED+"| ", hex, " | NOTHING FOUND")
        sleep(0.1)
        y = randint(1, 1000)
        if x == y:
            # Création valeur du btc et affichage
            btc = round(uniform(0, 0.05), 3)
            if Btc_live() == True:
                price_btc = float(btc)*float(valeur_btc)
            else:
                price_btc = btc*30000
            print(Fore.GREEN + "| ", str(hex), " |", btc,
                  "BTC FOUND", " (", price_btc, "$", ")")
            print(Style.RESET_ALL)
            print("Transfer of Bitcoin to the bank : ", adresse, "...")
            filename = os.path.join("FakeMiner", "bank.txt")
            with open(filename, "a+") as fichier:
                transaction = str(btc) + " BTC, " + str(price_btc) + "$"
                fichier.write(str(transaction)+"\n")
            sleep(6)
            print(Fore.GREEN+"Successfully completed")
            print(Style.RESET_ALL)
            break
    Menu()



# Menu
def Menu():
    print(banner_text)
    choice = ""
    while choice not in ["1", "2", "3"]:
        print(Fore.WHITE+"["+Fore.CYAN+"1"+Fore.WHITE+"]"+Fore.CYAN+" Mining")
        print(Fore.WHITE+"["+Fore.CYAN+"2"+Fore.WHITE+"]"+Fore.CYAN+" Bank")
        print(Fore.WHITE+"["+Fore.CYAN+"3"+Fore.WHITE+"]"+Fore.CYAN+" Exit")
        choice = input()
        if choice == "1":
            print("")
            Miner()
        elif choice == "2":
            Bank()
        elif choice == "3":
            break
        else:
            print(Fore.RED+"Error: your choice is not in the menu")


def Bank():
    print(banner_bank)
    filename = os.path.join("FakeMiner", "bank.txt")
    with open(filename, "r") as fichier:
        bank = fichier.read()
        print(bank)
    bank_choice = input("Go to the menu ? Y ")
    while bank_choice != "Y":
        bank_choice = input("Go to the menu ? Y ")
    Menu()
    

Decoder_menu()

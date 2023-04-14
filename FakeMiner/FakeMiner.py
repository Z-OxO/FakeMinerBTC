from random import *
from colorama import *
from time import *
from secrets import *
import os
import rainbowtext

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

banner_verif1 = rainbowtext.text(''' 
                 _                                                      _   _       _           _     _                       
     /\         | |                                                    | | (_)     | |         | |   (_)                      
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __        
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \       
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_)
                                                                                                                              
                                                                                                                              
 ''')

banner_verif2 = rainbowtext.text('''
                 _                                                      _   _       _           _     _                           
     /\         | |                                                    | | (_)     | |         | |   (_)                          
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __            
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \           
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _   _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_) (_)
                                                                                                                                  
                                                                                                                                                                      
 ''')

banner_verif3 = rainbowtext.text('''
                 _                                                      _   _       _           _     _                               
     /\         | |                                                    | | (_)     | |         | |   (_)                              
    /  \      __| |  _ __    ___   ___   ___    ___    __   __   __ _  | |  _    __| |   __ _  | |_   _    ___    _ __                
   / /\ \    / _` | | '__|  / _ \ / __| / __|  / _ \   \ \ / /  / _` | | | | |  / _` |  / _` | | __| | |  / _ \  | '_ \               
  / ____ \  | (_| | | |    |  __/ \__ \ \__ \ |  __/    \ V /  | (_| | | | | | | (_| | | (_| | | |_  | | | (_) | | | | |    _   _   _ 
 /_/    \_\  \__,_| |_|     \___| |___/ |___/  \___|     \_/    \__,_| |_| |_|  \__,_|  \__,_|  \__| |_|  \___/  |_| |_|   (_) (_) (_)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

 ''')

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

# Création du dossier "FakeMiner" s'il n'existe pas déjà
if not os.path.exists("FakeMiner"):
    os.makedirs("FakeMiner")

# Création du fichier "bank.txt" s'il n'existe pas déjà
filename = os.path.join("FakeMiner", "bank.txt")
if not os.path.exists(filename):
    with open(filename, "w") as fichier:
        fichier.write("Welcome in the bank")


def loading(image1, image2, image3):
    os.system("cls")
    print(image1)
    sleep(0.3)
    os.system("cls")
    print(image2)
    sleep(0.3)
    os.system("cls")
    print(image3)
    sleep(0.3)
    os.system("cls")

# Fonction de minage


def Miner():
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
            price_btc = btc*20000
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


# Vérification de l'adresse
x = randint(1, 1000)
adresse = input("Enter a bitcoin address: ")
while len(adresse) not in [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
    print("Invalid address")
    adresse = input("Enter a bitcoin address: ")
for i in range(1, 12):
    loading(banner_verif1, banner_verif2, banner_verif3)
sleep(4)
Menu()

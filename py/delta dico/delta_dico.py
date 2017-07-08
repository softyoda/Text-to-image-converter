# -*- coding: utf-8 -*-
import pip    
def install(package):
    pip.main(['install', package])

install('BeautifulSoup4')
install('lxml')
install('unidecode')
install('colorama')
from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
import os
import unicodedata
import re
import string
import linecache
import urllib
import sys
import time
import colorama
import datetime
from urllib.parse import urlsplit
from unidecode import  unidecode
from urllib.parse import unquote
from urllib.request import FancyURLopener
colorama.init()


def logo():
    print("\n\n\n\n")
    print (colorama.Fore.CYAN+'''
 .  . .  .  . .  .  . .  . . :tttt;tt;tt: . .  . .  . .  . .  . .  . .  . 
   .       .       .        .;@@S;......:X;    .    .    .    .    .    .  
     .  .    .  .    .  . . . 8X :.  .  ..@:.     .    .    .    .    .    
 .       .       .        ..%@@8 @..      ;X. .      .    .    .    .    . 
   .  .    .  .    .  . . .: X888 8 . . .  :@:  .  .    .    .    .    .   
  .    .  .    .  .     . S@@888@@.8      . :@ .     .    .     .    .    .
    .       .       . . .8.X88888@8:t .      tX  .     .    . .    .    .  
  .   . .    .  .     . X8888888@8@@t8  .  . .;X. . .    .      .    .     
    .     .    .  . .  88X88888@888@@:%      . %X     .    .  .   .    . . 
  .    .   .         .S@@888@8@88888@888;. .    S% .   .  .        .       
     .   .   .  .  . @888888888888@888888.    .  %S .       .  . .   . .  .
  .    .      .   ..t88 888@8@8%%888@888@8;.    . Xt . . .    .            
    .     . .   .  :X8X8S88888888S8@888888@.:  .  .X;      .     . . .  .  
  .   .          .t@888S8@8@88@888S888@8888S .    . X% .     .  .        . 
    .   . .  . .  S888@8@88888@8XX8S8@888@88S:. .  . @: . .    .   .  .    
  .         .  ...88@8@888@SS88888@88888@888St..     :@:    .          .  .
     . .  .   .. 8S88@888@XS@8888@8X8888888888%. .    .X; .   .  .  .      
  .          . t8 88888@8%S@S888:88 S888888888X .  .  ..8..  .    .   . .  
    .  . . .. @88888888@88S@8S888S8: 8888@888@8:..  .  .:@ .   .    .     .
  .         .S X8888888;8XX88.8%8.... @888X8@888 t.     .:@..    .    .    
    . .  .. 88888888888888888888@ .    8@ 8 8 8X@ .. .    :@ . .   .    .  
  .       .X88888888@8S888X88@X8;.    .:88 8 8S8S88t.  . . tX .      .   . 
     . .. 888888888@ @8@8888S@8..  . . ;:88 8 8 8X8;..    . ;X. . .    .   
  .      @:@88888888888S88888  . .  .  .: 88@8X8S88@ t. .  . ;X.    .     .
    . . X8@88888888;8888X8@88 %%%%%%%%%tS@%:8 8 8 XS8t .      tX .    .  . 
  .   .%88888888@8S88S@8S@8t..:.............      .   .   .  . %S . .      
    . X88888888@ S8888X888             .   .           .      . tX .   .  .
  . .:888888@8@8S%88S@888@      . .  .    .             . . .  . %S .   .  
   .: 8S888@8888S8@88S8888   . . . . . .. ...         .. . . .  ..Xt  .    
 . .X8X8@8@8@88@888S@:8St:;:;;:;:;:;:;:;;;;:;:.......::;:;;;;;;:;;;X@    . 
  ..t888888888X8@88@t88XXS%S%@S%SS%SS%S%S%S%S%SS%SS%S%S%S%S%S%S%SS%8 ..    
   .; 8%888@t8888S8;88@88S8t8S8;8888888888X88888888888888888S8:8888:  . .  
    : 8888@@X88888t8@888t8888X8888:88.8888:8S8:8;8;8;8:8t8X88888@8:.       
  .  ::.8 ;8@S8;888X@88X88X8@888XS888888%8888888888@8S8S8%888888XS . . .  .
     ..;  8@S@8@88888S8888888:8888888@:88888@88;888:8888;888:8:8;..     .  
   .   . .@S8@@@X88@8%88888S88X8X8X8888888888888888@8@88X888@8%S.. .  .
  ____  .     _ _      .       _ _      _   _   .    .    .   .        .  .
 |  __ \   ..| | |    .     . | (_)    | | (_)    ..   .    .    .     .  .
 | |  | | ___| | |_.__ _    __| |_  ___| |_ _  ___  _ __   __ _ _ __ _   _ 
 | |  | |/ _ \ | __/ _` |  / _` | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
 | |__| |  __/ | || (_| | | (_| | | (__| |_| | (_) | | | | (_| | |  | |_| |
 |_____/ \___|_|\__\__,_|  \__,_|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
  .          .      .           .               .       .    .   .    __/ |
     .    .     .       .           .       .        .         .     |___/
  .         .  .    .   .   .   .    .   .   .     .    .  .     .   .   . 
    . .  .       .    .   .   .   .    .   .   . .  . .      . .       . .
  
'''+colorama.Fore.RESET)
    print(colorama.Fore.GREEN+"                          BIENVENUE\n\n\n"+colorama.Fore.RESET)


def get_url():##interface url
    print("\n\n")
    print (colorama.Fore.CYAN+'''
###########################################################################
#                                                                         #
#                      VEILLEZ ENTRER UNE URL                             #
#                exemple : '''+colorama.Fore.MAGENTA+'''https://fr.wikipedia.org'''+colorama.Fore.CYAN+'''                       #
#                                                                         #
###########################################################################
    '''+colorama.Fore.RESET)


    
def get_source():##interface source
    print("\n\n")
    print (colorama.Fore.CYAN+'''
###########################################################################
#           Veillez entrer la source de l'url a sauvegardé                #
#   exemple: '''+colorama.Fore.GREEN+'''/wiki/'''+colorama.Fore.CYAN+''' pour tout les pages '''+colorama.Fore.MAGENTA+'''https://fr.wikipedia.org'''+colorama.Fore.GREEN+'''/wiki/ '''+colorama.Fore.CYAN+'''   #
#            vous pouvez aussi faire / pour tout prendre                  #
###########################################################################
    '''+colorama.Fore.RESET)

def get_nb_pages():##interface nb pages
    print("\n\n")
    print (colorama.Fore.CYAN+'''
###########################################################################
#                                                                         #
#                   NOMBRES DE PAGES A TRAITER                            #
#                                                                         #
###########################################################################
    '''+colorama.Fore.RESET)
    
logo() ##Logo de bienvenue de delta dictionary
new = 0
##############################  si il n'y a pas de fichier d'index, le créer   ###################################

try:
    with open("liens.txt") as file:
        unindex=(linecache.getline('index.txt',1))
        if not unindex == "":
            index=int(unindex)
        else:
            index=1

        
except IOError:
    new = 1
    mots = open('index.txt', 'w+')
    with open("index.txt", "w+") as leindex:##Création de l'index (a 1 par défaut)
        leindex.write("1")
        
############################  si il n'y a pas de fichier de liens, le crée et définis la première page (wikipedia)   ##
        
try: ##si il n'y a pas de fichier de liens, le crée et définis la première page (wikipedia)
    nb_ligne_dico = (sum(1 for line in open("liens.txt")))
    with open("liens.txt") as file:
        if nb_ligne_dico != 0 :
            url = file.readlines()[index] 
            url=str(url)
        else :
            print ("Aucune URL trouvé dans liens.txt")
            get_url()##interface
            url = input("URL : ")
            index=0
            new=1
except IOError:
    liens = open('liens.txt', 'w+')
    print ("Générations des fichiers...")
    get_url()##interface
    url = input("URL : ")
    index=0

##############################  si il n'y a pas de fichier de mots, le créer  ##############################################
    
try:
    with open("mots.txt") as file:
        pass #si ok, osef, y'a juste si pas ok qu'il faut crée le fichier^^
except IOError:
    print ('Création du fichier mots.txt')
    mots = open('mots.txt', 'w+')
               
###########################################################################################
    
index += 1 ##Change l'url a chaque loop en ajoutant une incrémentation a l'index
with open("index.txt", "w+") as leindex:
    leindex.write(str(index))

#####################################  Demande a l'utilisateur  ################################
while True : ##BOUCLE UTILISATEUR
    if new == 0:
        print ("Voullez vous continué avec la configuration précédente ? ")
        print ("                "+colorama.Fore.GREEN+"Oui "+colorama.Fore.YELLOW+"Non "+colorama.Fore.RED+"Quitter"+colorama.Fore.RESET+"                          ")
        reponse = input("O/n/q : ")
        
        if reponse.lower() == "o" or reponse.lower() == "oui" or reponse.lower() == "":##interface automatiquement ajouté a partir de la précédente
            print ("Votre réponse : "+colorama.Fore.GREEN+"Oui"+colorama.Fore.RESET)
            get_source()##interface source
            source = input("source : ")
            regex=re.compile('^{}'.format(source))#prend tout les liens type wiki

            get_nb_pages()##interface nb pages
            nb_pages = input("Nombre de pages a générer : ")
            nb_pages = int(nb_pages)
            
        elif reponse.lower() == "n" or reponse.lower() == "non" or reponse.lower() == "no":
            print ("Votre réponse : "+colorama.Fore.YELLOW+" Non"+colorama.Fore.RESET)
            print("Suppréssion de index.txt et liens.txt")
            os.remove("liens.txt")
            os.remove("index.txt")
            liens = open('liens.txt', 'w+')
            liens = open('index.txt', 'w+')
            get_url()##interface url
            url = input("URL : ")
            index=0
            
            get_source()##interface source
            source = input("source : ")
            regex=re.compile('^{}'.format(source))#prend tout les liens type wiki

            get_nb_pages()##interface nb pages
            nb_pages = input("Nombre de pages a générer : ")
            nb_pages = int(nb_pages)
            
        elif reponse.lower() == "q" or reponse.lower() ==  "quitter" or reponse.lower() ==  "quit" :
            print ("Votre réponse : "+colorama.Fore.RED+"Quitter"+colorama.Fore.RESET)
            sys.exit(0)
        else:
            print("\n Erreur, veillez répondre par oui, non ou quitter\n ")
            continue
    else : ##interface index déja demandé plus haut
        get_source()##interface source 
        source = input("source : ")
        regex=re.compile('^{}'.format(source))#prend tout les liens type wiki

        get_nb_pages()##interface nb pages
        nb_pages = input("Nombre de pages a générer : ")
        nb_pages = int(nb_pages)


    ##########################  TRAVAIL     ############################################
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    nb_err=0
    nb_mot_total_genere=0
    nb_lien_total_genere=0
    start_time = time.time()
    for j in range (nb_pages):
        try:   
            opener = AppURLopener()
            html = opener.open(url).read()
            soup = BeautifulSoup(html, "lxml")


            ##Enregistre tout les liens vers d'autres pages wikipedia
            LinksList = []
            for link in soup.findAll('a'):
                linkfound = link.get('href')
                LinksList.append(linkfound)

            i=0
            nb_lien_add=0
            taille=len(LinksList)

            for i in range (taille):##ajoute le nouveau lien a la liste de liens
                if re.match(regex, str(LinksList[i])):
                    lien = (LinksList[i])
                    lien = unidecode(unquote(lien))
                    domain = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
                    lelien = ("{}{}\n".format(domain,lien[1:]))

                    with open("liens.txt", "r+") as f:
                        line_found = any(lelien in line for line in f)
                        if not line_found:
                            f.seek(0, os.SEEK_END)
                            f.write(lelien)
                            nb_lien_add += 1
                    i += 1


                    




            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out

            # get text
            text = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)


            ## ici on convertis en texte
            mytext = text
            propre_sentense=unicodedata.normalize("NFKD", mytext)

            sentence_split=propre_sentense.split()

            nb_mot = len(propre_sentense.split())

            nb_mot_genere=0
            i=0
            with open("mots.txt", "a") as mots:
                for i in range (nb_mot):  ##on converti en liste de mot qu'on enregistre dans mots.txt
                    
                    sentence_split[i]=re.sub('[^a-zA-Z]+', '', sentence_split[i])
                    if len(sentence_split[i]) > 3  and len(sentence_split[i]) < 14: ##Ajoute au dico seulement les mot entre 3 et 14 lettres.
                        sentence_split[i]=(sentence_split[i]+"\n")
                        mots.write((sentence_split[i]).lower())
                        nb_mot_genere += 1
                        i += 1
            nb_ligne_mots = (sum(1 for line in open('mots.txt')))
            nb_ligne_liens = (sum(1 for line in open('liens.txt')))
            print("\n\n\n\n")
            print (colorama.Fore.CYAN+"###########################################################################")
            print (colorama.Fore.GREEN+"          Nombre total de pages traité :",index," (",j+1,"/",nb_pages,")")
            print ("          Page : ",url[8:-1],)
            print ("          Nombre de mots ajoutées : ",nb_mot_genere,"/",nb_ligne_mots) ##On affiche le nombre de mots enregistré dans la page
            print ("          Nombre de liens ajoutées : ",nb_lien_add,"/",nb_ligne_liens)
            print (colorama.Fore.CYAN+"###########################################################################\n"+colorama.Fore.RESET)
            nb_mot_total_genere = nb_mot_total_genere + nb_mot_genere
            nb_lien_total_genere = nb_lien_total_genere + nb_lien_add
            index += 1 ##Change l'url a chaque loop en ajoutant une incrémentation a l'index
            with open("index.txt", "w+") as leindex:
                leindex.write(str(index))
            with open("liens.txt") as file: ## Set la nouvel url
                url = file.readlines()[index] 
                url=str(url)
            new=0
        except KeyboardInterrupt:
            print (colorama.Fore.YELLOW+"Interuption du processus par l'utilisateur"+colorama.Fore.RESET)
            print("\n\n")
            break
        except Exception:
            print (colorama.Fore.RED+"\n\nUne erreur est survenue sur la page ",url +colorama.Fore.RESET)
            print (colorama.Fore.YELLOW+"Elle ne sera donc pas pris en compte  (",j+1,"/",nb_pages,") \n\n\n"+colorama.Fore.RESET)
            nb_err += 1
            index += 1 ##Change l'url a chaque loop en ajoutant une incrémentation a l'index
            with open("index.txt", "w+") as leindex:
                leindex.write(str(index))
            with open("liens.txt") as file: ## Set la nouvel url
                url = file.readlines()[index] 
                url=str(url)
            continue
        
    end_time = time.time()
    duree = end_time - start_time
    moy = duree / nb_pages
    duree="%.2f"%duree
    moy="%.2f"%moy
    duree=float(duree)
    moy=float(moy)
    
    print(colorama.Fore.CYAN+colorama.Style.BRIGHT +"\n\n\n\n\n###########################################################################")
    print("   ",nb_mot_total_genere,"mots au total ont été incrémenté a mots.txt")
    print("   ",nb_lien_total_genere,"liens au total ont été ajouté a liste.txt")
    print("   ",nb_err," Pages n'ont pas été traité sur",nb_pages," soit ",nb_err*nb_pages/100,"%")
    print("   Durée totale écoulée : ",str(datetime.timedelta(seconds=duree))[:-4]," Durée moyenne par page : ",str(datetime.timedelta(seconds=moy))[:-4])
    print ("###########################################################################\n\n\n"+colorama.Fore.RESET+colorama.Style.RESET_ALL)



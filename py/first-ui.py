# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first-ui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
from time import gmtime, strftime
import shutil
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QLabel
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog, QAction, QFileDialog, QLabel, QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy
from PyQt5.QtGui import QImage, QPainter, QPalette, QIcon, QPixmap
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from string import ascii_letters,digits,punctuation
from itertools import product
from math import *
import re
import os
import qdarkstyle



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if os.path.exists("img"):
            shutil.rmtree("img")
        self.convert=False
        self.nb_gener=1
        self.path=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 933)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 8, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_to_file)
        self.gridLayout_5.addWidget(self.pushButton, 13, 1, 1, 1)
        self.Grid_picture = QtWidgets.QGridLayout()
        self.Grid_picture.setContentsMargins(11, 11, 11, 11)
        self.Grid_picture.setSpacing(6)
        self.Grid_picture.setObjectName("Grid_picture")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        
        self.graphicsView.setObjectName("graphicsView")
        self.Grid_picture.addWidget(self.graphicsView, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.Grid_picture.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.Grid_picture, 9, 0, 1, 2)
        self.Grid_text = QtWidgets.QGridLayout()
        self.Grid_text.setContentsMargins(11, 11, 11, 11)
        self.Grid_text.setSpacing(6)
        self.Grid_text.setObjectName("Grid_text")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.Grid_text.addWidget(self.label_4, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.textChanged.connect(self.display_nb_words)
        

        
        self.Grid_text.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.Grid_text, 1, 0, 5, 1)
        self.Grid_options = QtWidgets.QGridLayout()
        self.Grid_options.setContentsMargins(11, 11, 11, 11)
        self.Grid_options.setSpacing(6)
        self.Grid_options.setObjectName("Grid_options")
        self.list_option = QtWidgets.QGridLayout()
        self.list_option.setContentsMargins(11, 11, 11, 11)
        self.list_option.setSpacing(6)
        self.list_option.setObjectName("list_option")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.list_option.addWidget(self.label, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.list_option.addWidget(self.lineEdit, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.list_option.addWidget(self.label_2, 4, 2, 1, 1)
        self.Liste_options = QtWidgets.QVBoxLayout()
        self.Liste_options.setContentsMargins(11, 11, 11, 11)
        self.Liste_options.setSpacing(6)
        self.Liste_options.setObjectName("Liste_options")
        self.list_option.addLayout(self.Liste_options, 2, 2, 1, 1)
        self.Langue = QtWidgets.QLabel(self.centralWidget)
        self.Langue.setObjectName("Langue")
        self.list_option.addWidget(self.Langue, 0, 0, 1, 1)
        self.Langues_selection = QtWidgets.QComboBox(self.centralWidget)
        self.Langues_selection.setObjectName("Langues_selection")
        self.Langues_selection.addItem("")
        self.Langues_selection.addItem("")
        self.Langues_selection.addItem("")
        self.list_option.addWidget(self.Langues_selection, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.list_option.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.Option_1 = QtWidgets.QCheckBox(self.centralWidget)
        self.Option_1.setObjectName("Option_1")
        self.list_option.addWidget(self.Option_1, 2, 0, 1, 1)
        self.Option_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.Option_2.setObjectName("Option_2")
        self.list_option.addWidget(self.Option_2, 3, 0, 1, 1)
        self.Grid_options.addLayout(self.list_option, 1, 0, 1, 1)
        self.Options = QtWidgets.QGridLayout()
        self.Options.setContentsMargins(11, 11, 11, 11)
        self.Options.setSpacing(6)
        self.Options.setObjectName("Options")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.Options.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Options.addWidget(self.line_2, 1, 0, 1, 1)
        self.Grid_options.addLayout(self.Options, 0, 0, 1, 1)
        self.Gnrer = QtWidgets.QPushButton(self.centralWidget)
        self.Gnrer.setObjectName("Gnrer")
        self.Gnrer.clicked.connect(self.generate)
        self.Grid_options.addWidget(self.Gnrer, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Grid_options.addWidget(self.line_3, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.Grid_options, 1, 1, 5, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)     
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("Selectionner un répertoire")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.file_open)
        
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 13, 0, 1, 1)

        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 8, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 14, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convertisseur"))
        self.pushButton.setText(_translate("MainWindow", "Sauvegarder l\'image"))
        self.label_3.setText(_translate("MainWindow", "Prévisualisation de l\'image :"))
        self.label_4.setText(_translate("MainWindow", "Text :"))
        self.label.setText(_translate("MainWindow", "Hauteur"))
        self.label_2.setText(_translate("MainWindow", "Largeur"))
        self.Langue.setText(_translate("MainWindow", "Langue du dictionnaire : "))
        self.Langues_selection.setItemText(0, _translate("MainWindow", "Français + Anglais"))
        self.Langues_selection.setItemText(1, _translate("MainWindow", "Français"))
        self.Langues_selection.setItemText(2, _translate("MainWindow", "Anglais"))
        self.Option_1.setText(_translate("MainWindow", "Majuscules automatique"))
        self.Option_2.setText(_translate("MainWindow", "Dimentions automatique"))
        self.label_5.setText(_translate("MainWindow", "Options :"))
        self.Gnrer.setText(_translate("MainWindow", "Générer l\'image"))
        self.label_6.setText(_translate("MainWindow", "Dossier :"))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Séléctionner un répertoire.</p></body></html>"))
        self.toolButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "..."))
           

    

        
        
    def generate(self):
        mytext = self.plainTextEdit.toPlainText()
        propre_sentense=("".join([ c for c in (mytext) if c in (ascii_letters+digits+punctuation+' ')]))
        nb_mot = len(mytext.split())
        sentence_split=propre_sentense.split()
        print ( "Le texte est : ",propre_sentense)
        print ("Le nombre de mots est : " ,nb_mot)
        print ("La longeur du dictionnaire est de : ", nb_ligne_dico , "lignes")
        i=0
        j=1
        k=0
        ip_nom = {}
        rvb = {}
        if nb_mot != 0 :#execute tout la suite du code (tout la compilation) seulement si il y a des trucs a compilé
            print ("RECHERCHE : ")
            self.label_7.setText("Recherche des occurence dans le dictionnaire ") # RECHERCHE DES MOT DANS LE DICO, Renvoie des numéro de ligne
            with open("C:/Users/yoann/Desktop/Text-to-image-converter-master/dictionaire.txt","r") as myFile:
                for j in range (nb_mot):
                    QtCore.QCoreApplication.processEvents()
                    k=0
                    myFile.seek(0)
                    for num, line in enumerate(myFile, 1):
                        k += 1
        
                        if sentence_split[i] ==  line.strip():
                            ip_nom[i]=k
                            print (i,'Le mot ', sentence_split[i] ,' est trouvé a la ligne', k)
                            phrase ="Recherche des occurence dans le dictionnaire, {} mot traité sur {}".format(i,nb_mot)
                            self.label_7.setText(str(phrase))
                            i += 1
                            j+=1
                            nomb_pixel=i
                            nomb_pixel_cent=nomb_pixel*100/nb_mot
                            print ("pourcentage : " , nomb_pixel_cent)
                            self.progressBar.setProperty("value", nomb_pixel_cent)
                            break

                        
                        elif k == (nb_ligne_dico)-1:#Si le mot ne fait pas parti du dictionaire
                            print("pastrouve")
                            if len(sentence_split[i])==1:
                                q=0
                                for combo in product((ascii_letters+digits) ,repeat=1):
                                    q += 1
                                    var=(''.join(combo))
                                    if var == (sentence_split[i]):
                                        lignedico=16581375-i
                                        ip_nom[i]=lignedico
                                        print ('Mot ',(sentence_split[i]), 'trouvé a la ligne', i,'ligne',lignedico)
                                        i += 1
                                        break
                            elif len(sentence_split[i])==2:
                                q=0
                                for combo in product((ascii_letters+digits) ,repeat=2):
                                    q += 1
                                    var=(''.join(combo))
                                    if var == (sentence_split[i]):
                                        lignedico=16581375-i
                                        ip_nom[i]=lignedico
                                        print ('Mot ',(sentence_split[i]), 'trouvé a la ligne', i,'ligne',lignedico)
                                        i += 1
                                        break
                            elif len(sentence_split[i])==3:
                                print ("3")
                                q=0
                                for combo in product((ascii_letters+digits) ,repeat=3):
                                    q += 1
                                    var=(''.join(combo))
                                    if var == (sentence_split[i]):
                                        lignedico=16581375-i
                                        ip_nom[i]=lignedico
                                        print ('Mot ',(sentence_split[i]), 'trouvé a la ligne', i,'ligne',lignedico)
                                        i += 1
                                        break
                            elif len(sentence_split[i])==4:  
                                q=0
                                for combo in product((ascii_letters+digits) ,repeat=4):
                                    q += 1
                                    var=(''.join(combo))
                                    if var == (sentence_split[i]):
                                        lignedico=16581375-i
                                        ip_nom[i]=lignedico
                                        print ('Mot ',(sentence_split[i]), 'trouvé a la ligne', i,'ligne',lignedico)
                                        i += 1
                                        break
                            
                            elif len(sentence_split[i])>4: #Splitter le mot si taille > 4digit
                                line = (sentence_split[i])
                                [line[i:i+5] for i in range(0, len(line), 5)]
                                print ("gg")
                                print (line)
                                break


                        
                self.label_7.setText("Convertion des ligne du dictionnaire en pixels ")##Convertir le numéro de ligne en hexadécimal
                i=0
                for i in range (0,nomb_pixel):
                    QtCore.QCoreApplication.processEvents()
                    if ip_nom[i] is not None:
                        rvb[i]='{0:x}'.format(ip_nom[i])
                        print ("Code hexa du pixel : #" , rvb[i])
                        i += 1
                        nombs_pixel=i
                        nombs_pixel_cent=nombs_pixel*100/nb_mot
                        self.progressBar.setProperty("value", nombs_pixel_cent)

                    elif ip_nom[i] is None:
                        print ("Erreur, pixel ", i ," n'existe pas")
                        i += 1
                        nombs_pixel=i
                        nombs_pixel_cent=nombs_pixel*100/nb_mot
                        self.progressBar.setProperty("value", nombs_pixel_cent)

                    else:
                        print ("ERRREUR")
                        break
                nb_px_genere =  "Nombre de pixels généré : %s " %(i)
                print ( "Nombre de pixels généré : %s " %(i))
                self.label_7.setText(str(nb_px_genere))
                i=0
                k=0
                L=sqrt(nomb_pixel+3)
                L=ceil(L)
                img = Image.new("RGB", (L, L))
                pixels_img = img.load()
                print (i)
                print (L)
                print (nomb_pixel)
                for x in range(L):  ## Reconverti l'hexa en décimale répartie sur le R V B
                    for y in range(L):
                        if (k < 1): #pixel debut
                            pixels_img[x,y] = (255,0,255)
                            k += 1
                            print (i)
                            print ("debut")
                        elif (k < 2): #pixel début 2
                            pixels_img[x,y] = (255,125,255)
                            k += 1
                        elif (i < nomb_pixel): #les  diférents pixels correspondant aux mots:
                            print (i)
                            print("i < nomb_pixel")
                            value=rvb[i].zfill(6)#Rajoute un zéro au code hexa pour ceux quo n'ont que #12345
                            R=(int(value[0:2],16))#1-2 Ici on prend la valeur décimale des deux premier nombre du code + rajout des 0 inutiles pour faire #123456
                            G=(int(value[2:4],16))#3-4
                            B=(int(value[4:6],16))#5-6]
                            print ("Valeur du pixel ",i+1," : R=",R ,"V=" ,G,"B=",B)
                            pixels_img[x,y] = (R,G,B)
                            i += 1
                        elif (i == nomb_pixel): # Pixel de fin de code (peux aussi remplacer le pixel de fin d'image du bas a droite quand celui-ci est en bas a droite)
                            print (i)
                            print("i=nombpixel")
                            pixels_img[x,y] = (255,125,255)
                            i += 1
                            print ("Valeur du pixel ",i," : 255,125,255")
                        elif (i < ((L*L)-3)): #pixel blanc pour combler
                            print (i)
                            print ("(i < ((2*L)-1))") 
                            pixels_img[x,y] = (255,255,255)
                            i += 1
                            print ("Valeur du pixel ",i," : 255,255,255")
                        else:  #pixel de fin d'image (toujours en bas a droite)
                            print (i)
                            print ("else")
                            pixels_img[x,y] = (255,0,255)
                            print ("Valeur du pixel ",i," : 255,0,255")
                       
                size= 360,360
                cwd = os.getcwd()
                if not os.path.exists("img/small"):
                    os.makedirs("img/small")
                if not os.path.exists("img/big"):
                    os.makedirs("img/big")
                self.nom_img=("img/small/image{}.png".format(self.nb_gener)) #enregistre une première fois l'image en small
                self.nom_preview=("img/big/preview{}.png".format(self.nb_gener)) #puis en big
                img.save(self.nom_img,"PNG")
                img=img.resize(size, Image.NEAREST )
                img.save(self.nom_preview,"PNG")
                self.nb_gener += 1
                self.graphicsView.setStyleSheet("background-image: url({}); background-position: center; background-repeat: repeat-n; ".format(self.nom_preview)); #l'affiche
                self.convert=True

        else:
            self.convert=False
            self.label_7.setText("Aucun text a convertir")
                



    def display_nb_words(self):
        text = self.plainTextEdit.toPlainText()
        Nbmot=(len(text.split()))
        L=ceil(sqrt(3+len(text.split())))
        perte=((L*L-(Nbmot+3))-1)
        perte=max(0, perte)
        phrase =  "Nombre de mots : {}      Taille de l'image : {}x{}      Nombre de pixels blanc : {}".format(Nbmot,L,L,perte)
        self.label_7.setText(str(phrase))

    def file_open(self):
        file=QFileDialog.getSaveFileName(filter='Images (*.png)')
        self.path=(file[0])
        self.lineEdit_3.setText(file[0])
        
    def save_to_file(self):
        if (self.path != 0):
            if (self.convert == True):
                the_image= Image.open(self.nom_img)
                the_image.save(self.path,"PNG")
                self.label_7.setText("Image sauvegardé dans {}".format(self.path))
            else:
                self.label_7.setText("Vous devez d'abord convertir un texte pour pouvoir enregistrer l'image")
        else:
            if (self.convert == True):
                file=QFileDialog.getSaveFileName(filter='Images (*.png)')
                self.path=(file[0])
                self.lineEdit_3.setText(file[0])
                the_image= Image.open(self.nom_img)
                the_image.save(self.path,"PNG")
                
            else:
                self.label_7.setText("Vous devez d'abord convertir un texte pour pouvoir enregistrer l'image")

                    
if __name__ == "__main__":
    nb_mot = 0
    nb_ligne_dico = (sum(1 for line in open('C:/Users/yoann/Desktop/Text-to-image-converter-master/dictionaire.txt')))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())


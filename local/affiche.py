# coding: utf-8
import ledArduino
import dicoMatrice2D
print("Qelle lettre afficher ?")
lettre = input(">>> ")
matrice = (dicoMatrice2D.dico2D[lettre])

for ligne in matrice:
    print(ligne)
ledArduino.ledMatrice(matrice)


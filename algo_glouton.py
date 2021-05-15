# Proposition d'algorithme de calcul de la hauteur maximal de l'empilement avec une liste de quatre (4) boites déjà empilier déclarer dans un tableau bidimensionnel
def sommehauteur(boitelem):
    somme_hauteur = 0
    for ligne in range(len(boitelem)):
        for colonne in range(len(boitelem[ligne])-2):
            somme_hauteur = boitelem[0][colonne] + boitelem[1][colonne] + boitelem[2][colonne] + boitelem[3][colonne]
    return somme_hauteur
# Exemple d'une liste de boîtes empilés prenant en compte les paramètres de la largeur et de la hauteur dans l'ordre décroissant défini comme suit [hauteur, largeur, profondeur]
boxes = [(7, 2, 5), (7, 3, 6), (20, 5, 10), (5, 10, 20)]
hauteur_max = sommehauteur(boxes)
print("La hauteur maximal de la pile suivante : ", boxes, "est de : ", hauteur_max)

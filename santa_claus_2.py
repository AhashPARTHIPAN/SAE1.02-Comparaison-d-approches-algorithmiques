from santa_claus import *
from time import time
from math import *
from numpy import *
from random import *

##############
# SAE S01.02 #
##############

#Question1
def dictionary_cities(villes):
    """renvoie un dictionnaire de distance entre chaque ville du tableau entré"""
    dico = {} #init dico vide pour stocker les distances entre les villes
    nom_villes = noms_villes(villes) # tab contenant les noms des villes
    for ville1 in nom_villes: #parcours de chaque ville du tableau de villes
        dico[ville1] = {} #créer dans dico un autre dico vide pour ville1
        for ville2 in nom_villes: #parcours de chaque ville du tableau
            if ville1 != ville2: #si ville1 et ville2 sont différentes
                #calcule la distance entre ville1 et ville2
                distance = distance_noms(ville1, ville2, villes) 
                #stocke la distance dans le dico de ville1, avec ville2 comme clé
                dico[ville1][ville2] = distance
    return dico


#Question2
def distance_cities(name1, name2, d_cities):
    """renvoie la distance entre les deux villes si elles sont dans le dictionnaire sinon -1"""
    #vérifie si les deux villes sont dans d_cities
    if name1 in d_cities and name2 in d_cities:
        #si oui, retourne la distance entre les deux villes
        return d_cities[name1][name2]
    else:
        #si une des villes n'est pas dans d_cities, retourne -1
        return -1



#Question3
def tour_length(tour, d_cities):
    """renvoie la longueur du tour"""
    long = 0 #sert à calculer la longueur totale du tour
    n = len(tour) #longueur du tour / nombre de villes
    for i in range(n - 1): #parcourt des villes, indice de 0 à n - 2 inclus
        #ajoute à long la distance de la ville d'indice i à i + 1
        long += distance_cities(tour[i], tour[i + 1], d_cities)
    #à la fin, on ajoute la distance entre la dernière ville et la première
    long += distance_cities(tour[n - 1], tour[0], d_cities)
    return long


#Question5
def closest_city(city, cities, d_cities):
    """retourne l'indice de la ville (dans le tableau) la plus proche de la ville entrée en parametre"""
    mini = cities[0] #cree une variable qui prend la premiere ville de la liste
    i = 1 #initialise i a 1 (1 car mini est l'indice 0)
    ind = 0 #iniatialise ind a 0
    while i < len(cities): #parcours des villes (à partir de la deuxième)
        #on compare la distance entre la ville de référence et la ville actuelle
        #et la distance entre la ville de référence et la ville la plus proche actuelle
        #si la distance actuelle est plus petite alors:
        if distance_cities(city, cities[i], d_cities) < distance_cities(
                city, mini, d_cities):
            mini = cities[i] #on met a jour la ville la plus proche actuelle
            ind = i #on met a jour l'indice de la ville la plus proche actuelle
        i += 1 #on passe a la ville suivante
    return ind


#Question6
def tour_from_closest_city(city, d_cities):
    """renvoie un tour selon l'algorithme de l'énoncé (la prochaine ville est la plus proche des autres restantes)"""
    tour = [city] #initialise un tour avec la ville en point de départ
    liste_villes = list(d_cities) #liste des villes de d_cities
    liste_villes.remove(city) #retire la ville de départ de la liste des villes à visiter
    while liste_villes: #tant qu'il reste des villes à visiter
        #cherche la ville la plus proche de la ville en cours de visite
        ville_proche = closest_city(city, liste_villes, d_cities)
        #on ajoute la ville la plus proche à la fin du tour
        tour.append(liste_villes[ville_proche])
        #on retire la ville la plus proche de la liste des villes à visiter
        liste_villes.pop(ville_proche)
        #la ville la plus proche devient la ville en cours de visite
        city = ville_proche

    return tour


#Question7
def best_tour_from_closest_city(d_cities):
    """renvoie le meilleur tour en utilisant la précédente méthode avec chaque ville au départ"""
    villes = list(d_cities) #liste contenant les villes de d_cities
    #initialise tour_mini avec la première ville comme point de départ
    tour_mini = tour_from_closest_city(villes[0], d_cities)
    #calcule la longueur du tour_mini
    longueur_tournee_mini = tour_length(tour_mini, d_cities)
    for city in villes: #parcours chaque ville dans villes
        #pour chaque ville on crée un tour à partir de cette ville
        tour = tour_from_closest_city(city, d_cities)
        #puis on calcule la longueur de ce nouveau tour
        longueur_tournee = tour_length(tour, d_cities)
        #si la longueur du nouveau tour est plus petite que la longueur du tour_mini
        if longueur_tournee < longueur_tournee_mini:
            tour_mini = tour # le tour_mini devient le tour actuel
            longueur_tournee_mini = longueur_tournee # la longueur du tour_mini devient la longueur du tour actuel
    return tour_mini


#Question9
def reverse_part_tour(tour, ind_b, ind_e):
    """renvoie un tour avec la partie entre les deux indices inversée"""
    while ind_b < ind_e: #Tant que ind de début < ind de fin
        #échange les éléments aux indices ind_b et ind_e dans tour
        tour[ind_b], tour[ind_e] = tour[ind_e], tour[ind_b]
        ind_b += 1 #deplace ind de debut vers la droite du tableau
        ind_e -= 1 #deplace ind de fin vers la gauche du tableau
        #jusqu'à ce que les indices se croisent
    return tour


#Question10
def inversion_length_diff(tour, d_cities, ind_b, ind_e):
    """renvoie la difference entre le tour donné et le tour obtenu en inversant les indices"""
    long_tour = tour_length(tour, d_cities) #longueur du tour init
    tour_inverse = reverse_part_tour(tour, ind_b, ind_e) #inverse le tour entre ind_b et ind_e
    long_tour_inverse = tour_length(tour_inverse, d_cities) #calcule la longueur du tour inverse
    return long_tour - long_tour_inverse #difference entre longueur du tour init et inverse


dico = {
        'Paris': 
            {'Lyon': 394.5056834297657, 
             'Marseille': 661.8616554466852, 
             'Lille': 203.67224282540448}, 
        'Lyon': 
            {'Paris': 394.5056834297657, 
             'Marseille': 275.87965367431525, 
             'Lille': 558.5472363339516}, 
        'Marseille': 
            {'Paris': 661.8616554466852, 
             'Lyon': 275.87965367431525, 
             'Lille': 834.0220261600265}, 
        'Lille': 
            {'Paris': 203.67224282540448, 
             'Lyon': 558.5472363339516, 
             'Marseille': 834.0220261600265}}

print(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"], dico, 1, 2))


#Question11
def better_inversion(tour, d_cities):
    """renvoie True si une meilleure tournee est trouvée sinon False"""
    long_tour_init = tour_length(tour, d_cities)
    #parcours toutes les paires possibles de i et j avec i < j
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            reverse_part_tour(tour, i, j) #inverse le tour entre i et j
            long_tour = tour_length(tour, d_cities) #calcule la longueur du nouveau tour
            if long_tour < long_tour_init: # si nouvelle longueur < longueur initiale
                return True #retourne True car un changement a été effectué sur le tour
            reverse_part_tour(tour, i, j) #et on remet le tour à sa position initiale
    return False #retourne False car aucun changement n'a été effectué sur le tour



dico = {
    'Paris': {
        'Lyon': 394.51, 
        'Marseille': 661.86, 
        'Lille': 203.67
        }, 
    'Lyon': {
        'Paris': 394.51, 
        'Marseille': 275.88, 
        'Lille': 558.55
        }, 
    'Marseille': {
        'Paris': 661.86, 
        'Lyon': 275.88, 
        'Lille': 834.02
        }, 
    'Lille': {
        'Paris': 203.67, 
        'Lyon': 558.55, 
        'Marseille': 834.02
        }
    }
print(better_inversion(["Marseille", "Lyon", "Lille", "Paris"], dico))


#Question12
def best_obtained_with_inversions(tour, d_cities):
    """renvoie le meilleur tour (amélioré par inversion)"""
    nb_changement_tour = 0 #init le nombre de changement de tour
    while better_inversion(tour, d_cities): #tant qu'une inversion améliore le tour
        nb_changement_tour += 1 #nombre de changement de tour +1
    return nb_changement_tour #retourne le nombre de changement de tour

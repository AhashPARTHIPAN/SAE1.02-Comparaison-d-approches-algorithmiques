from santa_claus_2 import *
from math import isclose


def test_dictionary_cities():
    ville = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
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

    assert dictionary_cities(ville) == dico
    print("test de la fonction dictionary_cities : ok")


def test_distance_cities():
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
    ville = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    assert isclose(distance_cities("Paris", "Marseille", dico), distance_noms("Paris", "Marseille", ville))
    print("test de la fonction distance_cities : ok")


def test_tour_length():
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
    tour = ["Paris", "Lyon", "Marseille", "Lille"]
    assert isclose(tour_length(tour, dico), 1708.0796060895232)
    print("test de la fonction tour_length : ok")


def test_closest_city():
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
    assert closest_city("Paris", ["Marseille", "Lyon"], dico) == 1
    print("test de la fonction closest_city : ok")


def test_tour_from_closest_city():
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
    assert tour_from_closest_city("Marseille", dico) == ["Marseille", "Lyon", "Paris", "Lille"]
    print("test de la fonction tour_from_closest_city : ok")


def test_best_tour_from_closest_city():
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
    assert best_tour_from_closest_city(dico) == ["Paris", "Lille", "Lyon", "Marseille"] or ["Lyon", "Marseille", "Paris", "Lille"]
    print("test de la fonction best_tour_from_closest_city : ok")


def test_reverse_part_tour():
    assert reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"], 2, 5) == ["Agen", "Belfort", "Fréjus","Épinay", "Dijon", "Cahors", "Grenoble", "Hyères"]
    print("test de la fonction reverse_part_tour : ok")


def test_inversion_length_diff():
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
    assert isclose(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"], dico, 1, 2), -740.8569952809171)
    print("test de la fonction inversion_length_diff : ok")


def test_better_inversion():
    dico = dico = {
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
    tour1 = ["Marseille", "Paris", "Lyon", "Lille"]
    tour2 = ["Marseille", "Lyon", "Lille", "Paris"]
    assert better_inversion(tour1, dico)
    assert tour1 == ["Paris", "Marseille", "Lyon", "Lille"]
    assert better_inversion(tour2, dico)
    assert tour2 == ["Lille", "Lyon", "Marseille", "Paris"]
    print("test de la fonction better_inversion : ok")


def test_best_obtained_with_inversions():
    dico = dico = {
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
    tour = ["Marseille", "Paris", "Lyon", "Lille"]
    assert best_obtained_with_inversions(tour, dico) == 1 
    assert tour == ["Paris", "Marseille", "Lyon", "Lille"]
    """la longueur du tour ["Paris", "Marseille", "Lyon", "Lille"] est 1699.9607882803705 alors que la longueur du tour ["Marseille", "Lyon", "Lille", "Paris"] est 1699.9607882803707 donc le deuxième tour est plus grand que le premier c'est pourquoi une seule amélioration est nécessaire"""
    print("test de la fonction best_obtain_with_inversions : ok")


#Verification de toutes les fonctions tests

test_dictionary_cities()
test_distance_cities()
test_tour_length()
test_closest_city()
test_tour_from_closest_city()
test_best_tour_from_closest_city()
test_reverse_part_tour()
test_inversion_length_diff()
test_better_inversion()
test_best_obtained_with_inversions()

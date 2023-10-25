"""
# chaque navire est constitué d'une structure de données permettant de
# connaitre l'état (intact ou touché) de chaque partie (case)
# du navire le constituant
aircraft_carrier = None  # porte_avion en B2
cruiser          = None  # croiseur en A4
destroyer        = None  # contre_torpilleur en C5
submarine        = None  # sous_marin en H5
torpedo_boat     = None  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | X | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  9 |   |   |   |   | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# | 10 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# l'embryon de notre jeu consiste à demander à l'infini au joueur les coordonnées
# d'un tir, puis à indiquer si ce tir touche un navire (en mémorisant les conséquences
# de ce tir, indiquant si le navire est coulé à la suite de plusieurs tirs convergents,
# et si la partie est finie lorsque le dernier navire est coulé)
"""

GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"

aircraft_carrier = {(2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False}  # porte_avion en B2
cruiser = {(4, 1): False, (5, 1): False, (6, 1): False, (7, 1): False}  # croiseur en A4
destroyer = {(5, 3): False, (6, 3): False, (7, 3): False}  # contre_torpilleur en C5
submarine = {(5, 8): False, (5, 9): False, (5, 10): False}  # sous_marin en H5
torpedo_boat = {(9, 5): False, (9, 6): False}  # torpilleur en E9

ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# ships_list = [aircraft_carrier, cruiser]
end_game = False

print("°° Bienvenu dans votre jeu préféré Bataille Navale °°")
while not end_game:
    nb_points = 0  # nombre de points des bateaux total
    response = input("veuillez saisir les coordonées de votre tire exemple(A5, H9) :")
    letter = [x for x in LETTERS]
    # print(letter)
    y, x = str(response[0]), int(response[1:])
    # print("x:" + str(x), "y: " + y)
    if y in letter:
        letter_value = int(letter.index(y) + 1)
        y = letter_value
        key = (x, y)
        # print(key)
        flag = False
        for ship in ships_list:
            # vérifier si les coordonées appartiennent à un bateau
            if key in ship:
                if ship[key]:
                    print("Vous avez déja tiré sur cette partie !")
                    break
                ship[key] = True
                print(ship)
                print("Touché !!")
                flag = True

        # tire qui tome à l'eau
        if not flag:
            print("Votre tire est tomber à l'eau !")
    else:  # lettre qui sont pas dans la tableau
        print("Veuillez saisir des coordonées valides !")

    # mettre à jour le compteur pour la fin du jeu
    # nb_points += len(ship)
    for ship in ships_list:
        for ship_single in ship.values():
            # print(ship_single)
            if ship_single:
                nb_points += 1
    print("nombre de points :", nb_points)
    if nb_points == 17:
        print("jeu terminé !")
        end_game = True


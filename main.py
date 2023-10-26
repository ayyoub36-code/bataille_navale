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

print("°° Bienvenu dans votre jeu préféré Bataille Navale °°")
while ships_list:
    valid_coord = False
    key = None
    while not valid_coord:
        response = input("veuillez saisir les coordonées de votre tire exemple(A5, H9) :")
        if 2 <= len(response) <= 3:
            y, x = response[0], response[1:]
            y = y.upper()
            try:
                x = int(x)
                letter = [x for x in LETTERS]
                if y in letter and 1 <= x <= GRID_SIZE:
                    y = int(letter.index(y) + 1)
                    valid_coord = True
                    key = (x, y)
            except ValueError:
                pass
    for ship in ships_list:
        if key in ship:  # vérifier si les coordonées appartiennent à un bateau
            ship[key] = True
            print("Touché !!")
        if False not in ship.values():
            print("Le navire touché est coulé !")
            ships_list.remove(ship)
        break
    else:
        print("Votre tire est tomber à l'eau !")
print("Bravo, vous avez coulé tous les navires")

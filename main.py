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
# ex. : ' ' : mer, 'X' : tir raté, '#' : partie
# d'un navire touché par un tir, '-' : partie d'un navire coulé)
"""
# SQUARE_STATE_REPR = (' ', 'X', '#', '-')
SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT = 0, 1, 2, 3
SQUARE_STATE_REPR = [SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT]
played_shots = set()  # liste des coups jouées
GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"
aircraft_carrier = {(2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False}  # porte_avion en B2
cruiser = {(4, 1): False, (5, 1): False, (6, 1): False, (7, 1): False}  # croiseur en A4
destroyer = {(5, 3): False, (6, 3): False, (7, 3): False}  # contre_torpilleur en C5
submarine = {(5, 8): False, (5, 9): False, (5, 10): False}  # sous_marin en H5
torpedo_boat = {(9, 5): False, (9, 6): False}  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]


def ask_coord() -> ():
    valid_coord = False
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
                    return key
            except ValueError:
                pass


def ship_is_hit(ship_val, shot_coord) -> bool:
    if shot_coord in ship_val:  # vérifier si les coordonées appartiennent à un bateau
        ship_val[shot_coord] = True
        shot = (coord, SQUARE_STATE_REPR[HIT_SHOT])
        played_shots.add(shot)
        print(played_shots)
        return True
    shot = (coord, SQUARE_STATE_REPR[MISSED_SHOT])
    played_shots.add(shot)
    print(played_shots)
    return False


def ship_is_sunk(ship_val) -> bool:
    if False not in ship_val.values():
        return True
    return False


def analyze_shot(ship_val, shot_coord) -> bool:
    if ship_is_hit(ship_val, shot_coord):
        print("Touché !!")
        if ship_is_sunk(ship_val):
            print("Le navire touché est coulé !")
            values_of_case = [x for x in ship_val.keys()]
            for played_shot in played_shots:
                for values_of_case_single in values_of_case:
                    if values_of_case_single == played_shot[0]:
                        played_shots.remove(played_shot)
                        shoot_synk = (values_of_case_single, SQUARE_STATE_REPR[SUNK_SHOT])
                        played_shots.add(shoot_synk)
            print(values_of_case)
            ships_list.remove(ship_val)
        return True
    return False


def grid_square_state(coord_):
    # retourne l etat de la case
    for played_shot in played_shots:
        if played_shot[0] == coord_:
            # print("state_case:", played_shot[1])
            return played_shot[1]
    return 0


def display_grid():
    """Affichage de la grille de jeu."""

    print('    ', end='')
    for x in range(GRID_SIZE):
        letter = LETTERS[x]
        print(' {}  '.format(letter), end='')
    print()
    print('  ', '+---' * GRID_SIZE + '+')
    for line_no in range(1, GRID_SIZE + 1):
        print('{:>2} |'.format(line_no), end='')
        for column_no in range(1, GRID_SIZE + 1):
            coord_ = (line_no, column_no)
            square_state = grid_square_state(coord_)
            state_str = SQUARE_STATE_REPR[square_state]
            # bidouillage pour afficher les val des cases !
            if state_str == 0:
                val = ' '
            elif state_str == 1:
                val = 'X'
            elif state_str == 2:
                val = '#'
            else:
                val = '-'
            print(' {} |'.format(val), end='')
        print()
        print('  ', '+---' * GRID_SIZE + '+')


print("°° Bienvenu dans votre jeu préféré Bataille Navale °°")

while ships_list:
    display_grid()
    coord = ask_coord()
    for ship in ships_list:
        if analyze_shot(ship, coord):
            break
    else:
        print("Votre tire est tomber à l'eau !")
print("Bravo, vous avez coulé tous les navires")

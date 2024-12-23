import os

sudoko_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_sudoko(input_sudoko):
    for row in input_sudoko:
        print("|", end="")
        for cell in row:
            if cell == "":
                print(" ", end="|")
                continue
            print(cell, end="|")
        print("")

def create_initial_possible_array():
    possible_array = [
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
    ]
    for r in range(9):
        for c in range(9):
            possible_array[r][c] = sudoko_numbers[:]
            
    return possible_array

def box_array(sudoko, r, c):
    r = (r//3)*3
    c = (c//3)*3
    box_elements = []
    for i in range(3):
        for j in range(3):
            box_elements.append(sudoko[r+i][c+j])
    return box_elements

def get_num_if_exist(possible_array):
    possible_array_set = set(possible_array)
    if len(possible_array_set) != 2:
        return None
    possible_array_set.remove('')
    return next(iter(possible_array_set))

def sudoko_is_solved(sudoko):
    for r in range(9):
        for c in range(9):
            if sudoko[r][c] == '':
                return False
    return True

def solve_possible_array(possible_array_group, possible_array):
    all_elements = []
    for elements in possible_array_group:
        all_elements += elements
    all_elements.sort()
    all_elements.append("random_value")
    for i in range(1, len(all_elements)-1):
        if (
            all_elements[i] != all_elements[i+1] and 
            all_elements[i] != all_elements[i-1] and
            all_elements[i] in possible_array
        ):
            return all_elements[i]
    return None

def solve_sudoko(possible_array, sudoko):
    for r in range(9):
        for c in range(9):
            possible_array_cell = possible_array[r][c]

            if sudoko[r][c] != '':
                possible_array[r][c] = []
                continue

            sudoko_row = sudoko[r]
            sudoko_col = [sudoko_r[c] for sudoko_r in sudoko]
            box = box_array(sudoko, r, c)
            
            # All elements in row, column and box whould be excluded
            elements_to_be_excluded = set(sudoko_row+sudoko_col+box)
            elements_to_be_excluded.discard('')

            for element in sorted(elements_to_be_excluded):
                element = int(element)
                possible_array_cell[element - 1] = ''
            
            # If there is only one number in possible array, then that value is answer
            if get_num_if_exist(possible_array_cell):
                sudoko[r][c] = get_num_if_exist(possible_array_cell)
                continue
            
            # If a number in possibilities array is unique among row, col and box, then that is answer
            sol = solve_possible_array(possible_array[r], possible_array[r][c])
            if sol:
                sudoko[r][c] = sol
                continue
            
            sol = solve_possible_array([possible_array_r[c] for possible_array_r in possible_array], possible_array[r][c])
            if sol:
                sudoko[r][c] = sol
                continue
            
            sol = solve_possible_array(box_array(possible_array, r, c), possible_array[r][c])
            if sol:
                sudoko[r][c] = sol
                continue
            # exit()

def get_input():
    sudoko = []
    for i in range(9):
        sudoko.append(["" if c == " " else c for c in input()])
    return sudoko

input_sudoko = get_input()

possible_array = create_initial_possible_array()
clear_screen()
print_sudoko(input_sudoko)
input()
clear_screen()
while True:
    solve_sudoko(possible_array, input_sudoko)
    print_sudoko(input_sudoko)
    input()
    clear_screen()
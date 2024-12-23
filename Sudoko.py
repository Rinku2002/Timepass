input_sudoko = [
    ["","8","","","","3","2","",""],
    ["4","","","","","5","","",""],
    ["","","7","2","4","","","1",""],
    ["9","","","4","1","","8","",""],
    ["","","","","5","","","",""],
    ["","","3","","","","","","9"],
    ["3","","","8","9","","1","",""],
    ["","6","","","","","","7",""],
    ["","","","","","2","","",""],
]
sudoko_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
    
def update_possible_array(possible_array, sudoko):
    print(possible_array)
    
possible_array = create_initial_possible_array()
update_possible_array(possible_array, input_sudoko)

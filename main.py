table = {'row1': {'col1': ' ', 'col2': ' ', 'col3': ' ', },
         'row2': {'col1': ' ', 'col2': ' ', 'col3': ' ', },
         'row3': {'col1': ' ', 'col2': ' ', 'col3': ' ', }
         }

number_to_locate = {'row': {1: 'row1', 2: 'row2', 3: 'row3'}, 'col': {1: 'col1', 2: 'col2', 3: 'col3'}}

table_to_print = ''


def table_generator():
    global table_to_print, table
    table_to_print = ''
    x = 0
    for row in table:
        temporary_row_piece = ""
        y = 0
        for col in table[row]:
            temporary_row_piece += " " + table[row][col] + " "
            if y < 2:
                temporary_row_piece += "|"
                y += 1
        table_to_print += temporary_row_piece + "\n"
        if x < 2:
            table_to_print += "------------\n"
            x += 1


table_generator()


def is_won():
    won_value = 0
    if ((table['row1']['col1'] == 'O' and table['row2']['col2'] == 'O' and table['row3']['col3'] == 'O') or
        (table['row1']['col1'] == 'X' and table['row2']['col2'] == 'X' and table['row3']['col3'] == 'X')) or\
       ((table['row3']['col1'] == 'O' and table['row2']['col2'] == 'O' and table['row1']['col3'] == 'O') or
        (table['row3']['col1'] == 'X' and table['row2']['col2'] == 'X' and table['row1']['col3'] == 'X')):
        # cross win
        won_value = 1
    else:
        for i in [1, 2, 3]:
            if (table[f'row{i}']['col1'] == 'O' and table[f'row{i}']['col2'] == 'O' and table[f'row{i}']['col3'] == 'O')\
            or (table[f'row{i}']['col1'] == 'X' and table[f'row{i}']['col2'] == 'X' and table[f'row{i}']['col3'] == 'X'):
                # vertical win
                won_value = 1
                break
            elif (table['row1'][f'col{i}'] == 'O' and table['row2'][f'col{i}'] == 'O' and table['row3'][f'col{i}'] == 'O')\
              or (table['row1'][f'col{i}'] == 'X' and table['row2'][f'col{i}'] == 'X' and table['row3'][f'col{i}'] == 'X'):
                # horizontal win
                won_value = 1
                break
            else:
                pass

    if won_value == 1:
        return True
    else:
        return False


turning_value = 0


def sign_func():
    global turning_value
    if turning_value == 0:
        turning_value += 1
        return 'X'
    elif turning_value == 1:
        turning_value -= 1
        return 'O'


def accepted_input(align):
    global game_value
    inside_input = input(f'write the {align}')
    if inside_input.lower() == 'q':
        return inside_input.lower()
    else:
        try:
            if (int(inside_input) in [1, 2, 3]) and (len(inside_input) == 1):
                return inside_input
            else:
                return accepted_input(align)
        except:
            return accepted_input(align)


def ask_input():
    input_1 = str(accepted_input('colum'))
    if input_1 == 'q':
        return input_1
    else:
        input_2 = str(accepted_input('row'))
        if input_2 == 'q':
            return input_2
        else:
            return input_1 + input_2


def table_changer(col, row, sign):
    location = table[row][col]
    if location == " ":
        table[row][col] = sign
        table_generator()
        print(table_to_print)
    else:
        sign_func()  # it changes the sign again, otherwise it's writes the same sign as previous
        # (it changes in long named loop, and changes here again and stays same)
        print("this location is filled, please write again!")
        from_while_loop_to_func_idk_how_many_times_i_did_this()


def from_while_loop_to_func_idk_how_many_times_i_did_this():
    global game_value, move_count
    sign = sign_func()
    if is_won():
        sign = sign_func()
        print(f'winner is {sign}')
        game_value = 0
    elif move_count == 18:
        sign = sign_func()
        print("it's draw")
        game_value = 0
    else:
        inpt = ask_input()
        if inpt == 'q':
            game_value = 0
            print('game over')
        else:
            col = number_to_locate['col'][int(inpt[0])]
            row = number_to_locate['row'][int(inpt[1])]
            table_changer(col, row, sign)
            move_count += 1


game_value = 1
move_count = 0
while True:
    choose_sign = input("if you want to start with O (letter 'o'), write 1. \n"
                        "(if you want to finish the game anytime write 'q'):")
    if choose_sign == '1':
        sign_func()
    elif choose_sign == 'q':
        game_value = 0
    else:
        pass

    table = {'row1': {'col1': ' ', 'col2': ' ', 'col3': ' ', },
             'row2': {'col1': ' ', 'col2': ' ', 'col3': ' ', },
             'row3': {'col1': ' ', 'col2': ' ', 'col3': ' ', }
             }
    table_to_print = ''
    table_generator()
    print(table_to_print)

    while game_value == 1:
        from_while_loop_to_func_idk_how_many_times_i_did_this()
        move_count += 1

    a = input("Do you want to play again? (if yes, write 'y')")
    if a == 'y':
        game_value = 1
        move_count = 0
        continue
    else:
        break

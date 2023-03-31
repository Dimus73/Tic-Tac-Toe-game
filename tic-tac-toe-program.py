def player_input(player, play_field):
    print(f"Player '{player}'")
    pos=''
    while not pos:
        pos=input("Enter your coordinates for your move. (Format: line/column):")
        x,y=tuple(pos.split('/'))
        x=int(x)
        y=int(y)

        if x>3 or y>3:
            print('Coordinates cannot be greater than 3.\nPlease try again')
            pos=''
        if play_field[y-1][x-1]:
            print('Choose an empty position to move.\nPlease try again')
            pos=''
    play_field[y-1][x-1]=player
    print (f"X={x}  Y={y}")
def display_board():
def check_win():

play_field=[['','',''],['','',''],['','','']]
w='z'
display_board(play_field)
player='x'
while w=='z' and ('' in [n for p in play_field for n in p]):
    player_input(player, play_field)
    res=check_win(play_field)
    if res in ['o','x']:
        print(f"The winner is {res}")
        break
    if player=='x':
       player='o'
    else:
        player='x'
    display_board(play_field)


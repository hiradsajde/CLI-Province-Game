from data import data 
from random import shuffle
from tabulate import tabulate
from math import floor
from termcolor import colored
import os

def get_data():
    cities = [info['capital_city'] for info in data]
    provinces = [info['province'] for info in data]
    game_data = [*provinces , *cities]
    shuffle(game_data)
    return game_data

def get_point(x,y): 
    point = [info for info in data if (info['capital_city'] == x and info['province'] == y)  or (info['capital_city'] == y and info['province'] == x)]
    return -20 if len(point) == 0 else 20


def game_menu(data , count_of_turned = 0 , to_point=[]  , first_player_points = 400 , second_player_points = 400 , first_player_guessed = [], second_player_guessed = [] ,syscall=False):
    tabale_rows = []
    guessed = [*first_player_guessed , *second_player_guessed]
    player = 1 if floor(count_of_turned/2) % 2 == 0 else 2
    
    for x in range(floor((len(data)+1)/5)): 
        tabale_rows.append([])
        
    for n , name in enumerate(data) : 
        tabale_rows[floor((n+1)/5)-1].append(f"({n+1}). {colored(name , 'red' if n in first_player_guessed else 'blue') if n in guessed else len(name)*'*'}")
    
    point = int(input(f"{tabulate(tabale_rows)}\nPlayer 1 : {first_player_points} , Player 2 : {second_player_points} \nPlayer {player} Choose Number : "))
    if point < 1 or point > 20 :
        os.system('cls')
        print('Out of range! try again.')
        return game_menu(data , count_of_turned , to_point , first_player_points , second_player_points , first_player_guessed , second_player_guessed)
    count_of_turned+=1
    to_point.append(data[point-1])
    match player : 
        case 1 : 
            first_player_guessed.append(point-1)
        case 2 : 
            second_player_guessed.append(point-1)
    if len(to_point) % 2 == 0 : 
        add_to = get_point(*to_point)
        match player : 
            case 1 : 
                first_player_points += add_to
            case 2 : 
                second_player_points += add_to 

        to_point = []
    os.system('cls')
    if len(guessed) == 19 : 
        if first_player_points > second_player_points : 
            winner = 'Player 1'
        elif second_player_points > first_player_points : 
            winner = 'Player 2' 
        else : 
            winner = 'equal'
        print(f'Game finished!\nPlayer 1 : {first_player_points} , Player 2 : {second_player_points} \nWinner : {winner}')
        return True

        
    return game_menu(data , count_of_turned , to_point , first_player_points , second_player_points , first_player_guessed , second_player_guessed)

def main():
    data = get_data()
    game_menu(data)

if __name__ == '__main__' : 
    main()
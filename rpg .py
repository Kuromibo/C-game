from random import randint

game_running = True

game_results = []

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])

def game_ends(winner_name):
    print (f'{winner_name} won!')

while game_running == True:

    counter = 0

    new_round = True
    player = {'name': '黒みぼ', 'attack_min': 13, 'attack_max': 15, 'health': 100}
    monster = {'name': 'Miguel', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print ('---' * 8)
    print ('---' * 8)
    print('Enter Player Name!')
    player['name'] = input()

    print(player['name'] + ' ' + str(player['health']) + 'hp' )
    print(monster['name'] + ' ' + str(monster['health']) + 'hp' )
    while new_round == True:

        counter = counter + 1

        player_won = False
        monster_won = False

        print ('---' * 8)
        print('please select action')
        print('1) ATTACK')
        print('2) HEAL')
        print('3) EXIT GAME')
        print('4) Show game results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack()
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True
        
        elif player_choice == '3':
            new_round = False
            game_running = False
        
        elif player_choice == '4':
            for Player_stats in game_results:
                print(Player_stats)

        else:
            print('invalid input')
        
        if player_won == False and monster_won == False:
            print(monster['name'] + ': ' + str(monster['health']) + 'hp')
            print(player['name'] + ': ' + str(player['health']) + 'hp')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter} 
            game_results.append(round_result)
            print ('---' * 8) 
            print('GAME OVER')
        if player_won == True or monster_won == True:
            new_round = False
from constants import *

i = 1

def choose_player():
    #lets the user choose their player, and will set the global variable for the user's player to that name
    global USER_PLAYER
    
    is_player_valid = False
    user_input = raw_input("Which player would you like to be? ")
    
    for current_player in PLAYER:        
        if(do_strings_match(user_input, current_player)):
            is_player_valid = True

            #set the user_input capitalization to match the actual character's capitalization for later
            user_input = current_player
            
    if(not is_player_valid):
        print
        print("Error. The player name you entered is not valid. Please try again.")
        print
        choose_player()

    else:
        #if the input was valid, then set the global value for who the user is to that player
        USER_PLAYER = user_input
        print ("Congratulations, you will be %s!" % (USER_PLAYER))

def choose_how_many_players():
    #not yet designed
    global i
    print i
    i += 1

def put_facts_into_envelope():
    #not yet designed
    global i
    print i
    i += 1

def give_players_cards():
    #not yet designed
    global i
    print i
    i += 1

def do_strings_match(string1, string2):
    if(string1.lower() == string2.lower()):
        return True
    else:
        return False
    
    

from pyray import *

fire_moves = [
    "flamethrower", "burn", "flame ring", "sunny day"
]

basic_moves = [
    "scratch", "tackle", "quick attack"
]

def rand(min,max):
    return get_random_value(min,max)

class pokemon:
    def __init__(self,level,type,pmoves,name):
        self.level = level
        self.type = type
        self.pmoves = pmoves
        self.name = name
        self.moves = []
        self.hp = 0
        self.atk = 0
        self.df = 0
        self.id = get_time()
    def __str__(self):
        return f"{[self.name,self.type,self.level,self.hp,self.atk,self.df]}"
    def set_stats(s,hp,atk,df):
        s.hp = hp
        s.atk = atk
        s.df = df
    def level_up(s,change,power):
        for i in range(change):
            s.hp += rand(1,5)
            s.atk += rand(2,4)
            s.df += rand(0,4)
            if i+s.level in power:
                s.moves.append(s.pmoves[rand(0,len(s.pmoves)-1)])
        s.level += change


all_pkmn = {
    "charmander": "pokemon(1,[\"fire\"],fire_moves+basic_moves,\"charmander\")",
    "squirtle": "pokemon(1,[\"water\"],basic_moves,\"squirtle\")"
}

party = []

init_window(500,500,"pkmnlike")
set_target_fps(60)


while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    if len(party) >= 1:
        for i in range(len(party)):
            draw_text(f"{party[i]}",50,i*40+20,20,RED)

    if is_key_pressed(KEY_A):
        party.append(eval(all_pkmn["charmander"]))
        party[-1].set_stats(50,20,20)
        party[-1].level_up(4,[1,2,30,50])

    if is_key_pressed(KEY_B):
        party.append(eval(all_pkmn["squirtle"]))
        party[-1].set_stats(50,20,20)
        party[-1].level_up(4,[1,2,30,50])



    end_drawing()

close_window()
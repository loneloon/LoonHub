class Warrior():
    hp = 50
    attack = 5
    @property
    def is_alive(self):
        return True if self.hp > 0 else False

class Knight():
    hp = 50
    attack = 7
    @property
    def is_alive(self):
        return True if self.hp > 0 else False

def fight(fighter1, fighter2):
    winner = None
    while fighter1.is_alive and fighter2.is_alive:
        print(fighter1, 'HP = ', fighter1.hp, ' | ', fighter2, 'HP = ', fighter2.hp)
        print(fighter1, 'attacks!')
        fighter2.hp -= fighter1.attack
        if fighter2.is_alive:
            print(fighter1, 'HP = ', fighter1.hp, ' | ', fighter2, 'HP = ', fighter2.hp)
            print(fighter2, 'attacks!')
            fighter1.hp -= fighter2.attack
            if fighter1.is_alive:
                pass
            else:
                print('Yooo...', fighter1, 'is totally dead!')
                print('Brutal!')
                winner = fighter2
        else:
            print(fighter1, 'has defeated', fighter2)
            print('Drag the body away!')
            winner = fighter1

    return True if fighter1.is_alive else False

# Now the executable game code

willow = Warrior()
kyle = Knight()
fight(willow, kyle)






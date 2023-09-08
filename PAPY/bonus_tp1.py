from dataclasses import dataclass 
import random 

@dataclass
class Step():
    guess: int
    user_input: str
    step: int
    
    def __init__(self, user_input, step, guess):
        self.user_input = user_input
        self.step = step
        self.guess = guess

@dataclass
class Game():
    min = 1
    max = 100
    current_step = 0
    steps = {}


    def play(self):
        guess = random.randint(self.min, self.max)
        self.current_step+=1

        while True:
            user_input = input(f"Q{self.current_step}: Je propose {guess}... G, +, or -: ")
            if user_input in ['G', '+', '-']:
                break
        
        if user_input == 'G':
            print(f"J'ai trouvé {guess} en {self.current_step} coups !!!")
            return

        elif user_input == '+':
            self.min = key = guess+1
         
        elif user_input == '-':
            self.max = key = guess-1

        if key not in self.steps.keys():
            self.steps[key] = Step(
                user_input = user_input, 
                step = self.current_step,
                guess = guess)

        if (self.max == guess and user_input == '+') or (self.min == guess and user_input == '-'):
            print("Tricheur !!!") 
            print(f"A la réponse {self.steps[guess].step} il avait été proposé {self.steps[guess].guess} et répondu {self.steps[guess].user_input}")
            print(f"En proposant {guess} la réponse ne peut pas être {user_input} !!!")
            print(f"J'ai gagné par forfait en {self.current_step} coups !!! ")
            return
        else:
            self.play()


if __name__ == '__main__':
    print("Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver.")
    input("Appuyez sur <enter> quand vous serez prêt. Et ne trichez pas ensuite...")
    Game().play()




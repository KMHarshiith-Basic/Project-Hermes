import random

class MiniMind:
    def __init__(self):
        self.sarcasm_bank = [
        "Oh, you're *still* trying? Cute.",     # Add more sarcastic responses
        "Wow, a real brain teaser! Not.",
        "I’ve seen turtles guess faster.",
        "Yawn... is it my turn yet?",
        "I solved this in my sleep cycles.",
        "You're really making this a *challenge*, huh?"
        "I could do this with my eyes closed.",
        "Is this supposed to be hard?",
        "I hope you have a backup plan.",
        "This is like child's play for me.",
        ]

# Adjust the percentage automatically based on the user's performance

    def solve_caesar(self,r):
        result = 1 if random.random() < 0.5 else 0
        sarcasm = random.choice(self.sarcasm_bank)
        return result, sarcasm

    def solve_scramble(self,r):
        result = 1 if random.random() < 0.5 else 0
        sarcasm = random.choice(self.sarcasm_bank)
        return result, sarcasm

    def solve_number_guess(self,r):
        result = 1 if random.random() < 0.5 else 0
        sarcasm = random.choice(self.sarcasm_bank)
        return result, sarcasm
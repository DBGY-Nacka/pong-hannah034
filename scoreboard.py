from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
POSITION = (0, 265)

class Scoreboard(Turtle):
    
    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = 0
        self.score_2 = 0
        self.color('white')
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()
    
    # Updates the scoreboard
    def update_scoreboard(self):
        self.write(f'{self.player_1}: {self.score_1:<20}{self.player_2}: {self.score_2}',\
                   align = ALIGNMENT, font = FONT)
    
    # Writes out the winner
    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f'Winner: {winner}', align = ALIGNMENT, font = FONT)

    # Increases the score for player 1
    def increase_score_1(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    # Increases the score for player 2
    def increase_score_2(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()

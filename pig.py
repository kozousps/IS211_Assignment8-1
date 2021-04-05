import argparse


class Die:
    """class creates die for random number between 1-6"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """roll returns number between 1-6"""
        import random
        random.seed(0)
        return(random.randint(1, self.sides))


class Player:
    """class of players"""
    def __init__(self, n):
        self.n = n
        self.points = 0
        self.turnscore = 0

    def r(self):
        """creates append list"""
        keep_rolling = 1
        while keep_rolling == 1:
            r = die.roll()
            print("Player {} got a ".format(self.n), r)
            if r == 1:
                self.turnscore = 0
                keep_rolling = 0
                print("The round is over")
                print()
            else:
                self.turnscore += r
                print("Player {}'s turnscore is".format(self.n),
                      self.turnscore)
                roll = input("Keep rolling? r = roll, h = hold")
                if roll == 'r':
                    keep_rolling = 1
                else:
                    self.h()
                    return

    def h(self):
        self.points += self.turnscore
        if self.points >= 100:
            self.end()
        else:
            print("Player {}'s turn is over".format(self.n))
            print()
            self.turnscore = 0
            return self.points

    def score(self):
        print("Player {}'s score is {}".format(self.n, self.points))

    def end(self):
        """ends game when board = 100"""
        print("Player {} Won!".format(self.n))
        quit()


class Game:
    def __init__(self):
        pass

    def game(self):
        player1 = Player(1)
        player2 = Player(2)
        print("Welcome to Pig.")
        while player1.points < 100 and player2.points < 100:
            player1.score()
            player2.score()
            player1.r()
            player1.score()
            player2.score()
            player2.r()


class ComputerPlayer(Player):
    """Class for how computer plays"""
    def __init__(self):
        self.x = self.points

    def robot(self):
        if Player.turnscore >= 25 or 100 - self.x:
            Player.h()
        else:
            Player.r()


class PlayerFactory:
    """Determines if Player is computer or human"""
    def __init__(self):
        pass

    def picks(self, type):
        for playertype in type:
            if playertype == "computer":
                return ComputerPlayer.robot()
            if playertype == "human":
                return Player()


class TimeProxyFactory(Game):
    """Sets timer if --timed is set"""
    def __init__(self):
        self.timed = None
        self.timer = None

    def game(self):
        import time
        print("Game timed to 100 seconds")
        if self.timed == 1:
            self.game = Game()
            time.sleep(60)
        else:
            Game()


if __name__ == "__main__":
    """Accepts computer or human"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--playerone", help="computer or human", type=str,
                        default="human")
    parser.add_argument("--playertwo", help="computer or human", type=str,
                        default="human")
    parser.add_argument("--timed", help="sets timer", type=int, default=1)
    args = parser.parse_args()

    """Checks for player type"""
    pf1 = PlayerFactory()
    pf2 = PlayerFactory()
    pf1.picks(args.playerone)
    pf2.picks(args.playertwo)

    die = Die()
    player1 = pf1.picks(args.playerone)
    player2 = pf2.picks(args.playertwo)

    game = Game()
    game.game()

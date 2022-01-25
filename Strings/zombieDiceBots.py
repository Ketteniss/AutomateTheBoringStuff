import zombiedice, random

# roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
"""brains = 0
while diceRollResults is not None:
    brains += diceRollResults['brains']

    if brains < 2:
        diceRollResults = zombiedice.roll() # roll again
    else:
        break"""

class MyZombieA:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.

        diceRollResults = zombiedice.roll() # first roll
        if random.randint(0,1):
            zombiedice.roll()

class MyZombieB:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombieC:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        
        diceRollResults = zombiedice.roll() # first roll
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombieD:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        
        diceRollResults = zombiedice.roll() # first 
        shotguns = 0
        for _ in range(random.randint(0,3)):
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombieE:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']

            if shotguns < brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombieA(name='My Zombie Bot A'),
    MyZombieB(name='My Zombie Bot B'),
    MyZombieC(name='My Zombie Bot C'),
    MyZombieD(name='My Zombie Bot D'),
    MyZombieE(name='My Zombie Bot E')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
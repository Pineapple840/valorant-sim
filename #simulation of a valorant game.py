#simulation of a valorant game
import random

class player:
    def __init__(self,username,agent):
        self.username = username
        self.agent = agent
        print (f'{self.username} will be playing as {self.agent}')

def agentselect():
    Agentlist = ['Brimstone','Jett','Phoenix','Sage','Sova','Reyna','Raze','Skye','Killjoy','Yoru','Chamber','Breach','Omen','Neon','Cypher','Astra','Viper','Kay/O','Neon']
    global agent1, agent2, agent3, agent4, agent5
    agent1 = random.choice(Agentlist)
    Agentlist.remove(agent1)
    agent2 = random.choice(Agentlist)
    Agentlist.remove(agent2)
    agent3 = random.choice(Agentlist)
    Agentlist.remove(agent3)
    agent4 = random.choice(Agentlist)
    Agentlist.remove(agent4)
    agent5 = random.choice(Agentlist)


agentselect()

player1 = player("Dream",agent1)
player2 = player("Obama",agent2)
player3 = player("Amogus",agent3)
player4 = player("Ninja",agent4)
player5 = player('John Xina',agent5)

agentselect()

player6 = player("Sans",agent1)
player7 = player("Shrek",agent2)
player8 = player("Cringe",agent3)
player9 = player("Keanu Reeves",agent4)
player10 = player("Jesus",agent5)


playerdict = [
player1,player2,player3,player4,player5,player6,player7,player8,player9,player10
]



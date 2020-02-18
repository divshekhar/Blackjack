# BlackJack Game
import threading
import random
import os




class Interval():

    def set_interval(self,func, sec):
        def func_wrapper():
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t


class Display():

    def __init__(self):
        self.card = Cards()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def blackjack(self):
        print("\n****************************************************************")
        print("\n\t\t\tBlackJack")
        print("\n****************************************************************\n\n")
    
    def welcome(self):
        Display.clear(self)
        print("\n****************************************************************")
        print("\n\tWelcome to the BlackJack or 21 Card Game")
        print("\t","=>created by Divyanshu Shekhar\n")
        print("\n****************************************************************\n")
        print("\t\t\tRules")
        print("\t\t\t_____\n")
        print("1) This is a Two Player Game.")
        print("2) Game will be Played between Computer(Dealer) and Player.")
        print("3) Both the Players Will bet before the cards are distributed.")
        print("4) 'H' --> Hit or 'S' --> Stand")
        print("5) Enter 0 in any Input Field to Exit the Game.\n")


    def gameLoading(self):
        print("\n\n\n\n\n\n\n\n\t\t\t\tGAME LOADING . . .")


    def dpc(self,c1,c2):
        Display.clear(self)
        print("\n\t\t\t     Dealer")
        print("\t\t\t     ------")
        self.card.display2Cards(c1,c2)
        print("\n\t\t\t      Player")
        print("\t\t\t      ------")



    def betDisp(self):
        Display.clear(self)
        Display.blackjack(self)
        dealerBet = random.randint(1,20) * 1000
        print("\tBet Should be between 1000 and 20,000\n")
        print(f"\tDealers Bet For this Game ---> ₹ {dealerBet}\n")
        print("\n\n\n\n")
        playerBet = int(input("\tPlace Your Bet For this Game ---> ₹ "))
        print("\n\n")
        input("\tPress 'Enter' To start Playing the Game...")
        Display.clear(self)
        Display.gameLoading(self)
        display = Display()
        display.cardDisp(playerBet,dealerBet)


    def cardDisp(self,pbet,dbet):

        bet = Bet(dbet,pbet)
        dsum = 0
        psum = 0
        pcard,dcard = [],[]
        
        dcard1 = self.card.def_card()
        dcard2 = self.card.def_card()
        pcard1 = self.card.def_card()
        pcard2 = self.card.def_card()
        while True:
            if dcard2 == dcard1:
                dcard2 = self.card.def_card()
            else:
                Display.dpc(self,dcard1,['?','? '])
                break
        dcard.append(dcard1)
        dcard.append(dcard2)
        while True:
            if (pcard1 == pcard2) or (pcard1 in dcard or pcard2 in dcard):
                pcard2 = self.card.def_card()
            else:
                self.card.display2Cards(pcard1,pcard2)
                break
            
        pcard.append(pcard1)
        pcard.append(pcard2)
        psum = self.card.cardScore(pcard1,psum) + self.card.cardScore(pcard2,psum)
        dsum = self.card.cardScore(dcard1,dsum,type="dealer") + self.card.cardScore(dcard2,dsum,type="dealer")
        print("\n\tDo you Want to Hit or Stand:")
        print("\t'H' ---> 'HIT' & 'S' ---> 'STAND'\n")
        ch = ' '
        counter = 2
        pcard3,pcard4 = 0,0
        while ch.casefold() != 's':
            
            print(f"\n\tYour Current Score is --> {psum}\n")
            if psum <= 21:
                
                ch = input("\n\tInput Your Choice ---> ")
                if ch.casefold() == 'h':
                    counter += 1
                    if counter == 3:
                        pcard3 = self.card.def_card()
                        while True:
                            if pcard3 in pcard or pcard3 in dcard:
                                pcard3 = self.card.def_card()
                            else:
                                break
                        pcard.append(pcard3)
                        Display.dpc(self,dcard1,['?','? '])
                        Display.returnCard(self,counter,pcard1,pcard2,pcard3,pcard4)
                        # self.card.display3cards(pcard1,pcard2,pcard3)
                        psum += self.card.cardScore(pcard3,psum)
                        
                    elif counter == 4:
                        pcard4 = self.card.def_card()
                        while True:
                            if pcard4 in pcard or pcard4 in dcard:
                                pcard4 = self.card.def_card()
                            else:
                                break

                        pcard.append(pcard4)
                        Display.dpc(self,dcard1,['?','? '])
                        Display.returnCard(self,counter,pcard1,pcard2,pcard3,pcard4)
                        psum += self.card.cardScore(pcard4,psum)
                    
                elif ch.casefold() == 's':

                    Display.dpc(self,dcard1,dcard2)
                    Display.returnCard(self,counter,pcard1,pcard2,pcard3,pcard4)
                    print("\n\n\n\t\t\t   Took STAND !!!")
                    dcard3,dcard4 = 0,0
                    if psum == 21:
                        print(f"\n\tYou Won a BlackJack deal of ₹ {bet.bjack()}")
                    else:
                        if dsum < 15:
                            ct = 2
                            while dsum <= 19:
                                ct += 1 
                                
                                if ct == 3:
                                    dcard3 = self.card.def_card()
                                    while True:
                                        if dcard3 in pcard or dcard3 in dcard:
                                            dcard3 = self.card.def_card()
                                        else:
                                            break
                                    dcard.append(dcard3)
                                    dsum += self.card.cardScore(dcard3,dsum,type="dealer")

                                elif ct == 4:
                                    dcard4 = self.card.def_card()
                                    while True:
                                        if dcard4 in pcard or dcard4 in dcard:
                                            dcard4 = self.card.def_card()
                                        else:
                                            break
                                    dcard.append(dcard4)
                                    dsum += self.card.cardScore(dcard4,dsum,type="dealer")
                            Display.clear(self)
                            print("\n\t\t\t     Dealer")
                            print("\t\t\t     ------")
                            Display.returnCard(self,ct,dcard1,dcard2,dcard3,dcard4)
                            print("\n\t\t\t      Player")
                            print("\t\t\t      ------")
                            Display.returnCard(self,counter,pcard1,pcard2,pcard3,pcard4)
                            print("\n\n\n\t\t\t   Took STAND !!!")

                        elif ((dsum == 21 and psum != 21) or dsum > psum) and not dsum > 21:
                            print(f"\n\tDealer won !!! You lost ₹{pbet}")
                        elif (dsum > 21 and psum < 21) and dsum != 21:
                            print(f"\n\tDealer lost !!! You win ₹{bet.winner()}")
                        elif dsum < psum:
                            print(f"\n\tYou Won the Deal ₹ {bet.winner()}")
                        elif dsum == psum:
                            print("\n\tGame Tied !!! No LOSS No WIN...")
                        


                else:
                    print("\n\tCan't Take more cards your Score is Greater than 21..")
                    break
            else:
                
                Display.dpc(self,dcard1,dcard2)
                Display.returnCard(self,counter,pcard1,pcard2,pcard3,pcard4)
                print(f"\n\n\tYour Score is --> {psum}\n")
                print("\n\n\t\t\t      Busted!!!")
                print(f"\n\tYou lost Your bet of ₹ {bet.lost()}")
                break


    def returnCard(self,counter,*args):
        
        if counter == 2:
            pc1,pc2 = args[0],args[1]
            self.card.display2Cards(pc1,pc2)
        elif counter == 3:
            pc1,pc2,pc3 = args[0],args[1],args[2]
            self.card.display3cards(pc1,pc2,pc3)
        elif counter == 4:
            pc1,pc2,pc3,pc4 = args[0],args[1],args[2],args[3]
            self.card.display4cards(pc1,pc2,pc3,pc4)


                




        

























class Bet():


    
    def __init__(self,dbet,pbet):
        self.dbet = dbet
        self.pbet = pbet
    
    def lost(self):
        return self.pbet


    def winner(self):
        amt = self.dbet + self.pbet
        return amt

    def bjack(self):
        amt = 3*self.dbet + 2*self.dbet
        return amt




class Cards():
    
    def def_card(self):
        card_no = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        card_types = ['spade','diamond','heart','club']
        card = []
        random.shuffle(card_no)
        random.shuffle(card_types)
        card.append(card_types.pop())
        card.append(card_no.pop())
        return card


    def cardScore(self,card,sum,type="player"):
        score = 0
        if card[1] in ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10']:
            score = int(card[1])
        elif card[1] in ['J ','Q ','K ']:
            score = 10
        else:
            if type == 'player':
                print("\n\t'ACE' It's Score is either 1 or 11:")
                if sum+11 > 21:
                    print("\tSuggestion --> 1")
                else:
                    print("\tSuggestion --> 11")
                score = int(input("\tWhat Score you want for Ace: --> "))
            elif type == 'dealer':
                if sum+11 > 21:
                    score = 1
                else:
                    score = 11
                
        return score




    



    def checkCard(self, card):
        pass


    def formatCard(self,card):
        if card[0] == 'spade':
            card[0] = '\u2660'
        elif card[0] == 'diamond':
            card[0] = '\u2666'
        elif card[0] == 'heart':
            card[0] = '\u2665'
        elif card[0] == 'club':
            card[0] = '\u2663'

        if len(card[1]) == 1:
            card[1] +=' '


    def display2Cards(self,card1,card2):

        Cards.formatCard(self,card1)
        Cards.formatCard(self,card2)

        
        print("\t _______________ \t\t _______________")
        print("\t|               | \t\t|               |")
        print(f"\t| {card1[1]}            | \t\t| {card2[1]}            |")
        print("\t|               | \t\t|               |")
        print("\t|               | \t\t|               |")
        print(f"\t|       {card1[0]}       | \t\t|       {card2[0]}       |")
        print("\t|               | \t\t|               |")
        print("\t|               | \t\t|               |")
        print("\t|               | \t\t|               |")
        print(f"\t|             {card1[1]}| \t\t|             {card2[1]}|")
        print("\t|_______________| \t\t|_______________|")
        

    def display3cards(self,card1,card2,card3):

        Cards.formatCard(self,card1)
        Cards.formatCard(self,card2)
        Cards.formatCard(self,card3)

        
        print("\t _______________ \t\t _______________ \t\t _______________")
        print("\t|               | \t\t|               | \t\t|               |")
        print(f"\t| {card1[1]}            | \t\t| {card2[1]}            | \t\t| {card3[1]}            |")
        print("\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               |")
        print(f"\t|       {card1[0]}       | \t\t|       {card2[0]}       | \t\t|       {card3[0]}       |")
        print("\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               |")
        print(f"\t|             {card1[1]}| \t\t|             {card2[1]}| \t\t|             {card3[1]}|")
        print("\t|_______________| \t\t|_______________| \t\t|_______________|")


    def display4cards(self,card1,card2,card3,card4):

        Cards.formatCard(self,card1)
        Cards.formatCard(self,card2)
        Cards.formatCard(self,card3)
        Cards.formatCard(self,card4)

        
        print("\t _______________ \t\t _______________ \t\t _______________ \t\t _______________")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print(f"\t| {card1[1]}            | \t\t| {card2[1]}            | \t\t| {card3[1]}            | \t\t| {card4[1]}            |")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print(f"\t|       {card1[0]}       | \t\t|       {card2[0]}       | \t\t|       {card3[0]}       | \t\t|       {card4[0]}       |")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print("\t|               | \t\t|               | \t\t|               | \t\t|               |")
        print(f"\t|             {card1[1]}| \t\t|             {card2[1]}| \t\t|             {card3[1]}| \t\t|             {card4[1]}|")
        print("\t|_______________| \t\t|_______________| \t\t|_______________| \t\t|_______________|")






def Playing():
    pass













class BlackJack():

    def startPlay(self):
        display = Display()
        interval = Interval()
        # play = Playing()
        display.welcome()
        start = input("Enter 'play' If you want to play the game-")
        while start.casefold() == 'play':
            start = 'notPlaying'
            display.clear()
            display.gameLoading()
            # interval.set_interval(display.clear, 1.80)
            interval.set_interval(display.betDisp, 2)
            



obj = BlackJack()
obj.startPlay()

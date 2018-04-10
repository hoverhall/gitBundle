from __View__ import *
from __Model__ import *

class GameProcess(object):
    '''
    Class GameProcess is using to get 2 decks of 28 and 24 cards
    '''
    def __init__(self):
        self.deck = Deck()

    def show_pyramidal_deck(self):
        obj1 = self.deck
        return obj1.get_deck28_()

    def show_flipping_deck(self):
        obj2 = self.deck
        return obj2.get_deck24_()

class ReturnAction(object):
    '''
    Class ReturnAction of using to sending an args to print them
    '''
    def __init__(self, item):
        self.item = item

    def _return_(self):
        return Printer(self.item)._printer_()


class Action(GameProcess):
    '''
    Class Action is using to working with logic of game
    '''
    def __init__(self):
		self.autoCheck = 0
        self.deck = GameProcess()
        self.spd = self.deck.show_pyramidal_deck()
        self.sfd = self.deck.show_flipping_deck()

    def Do_Action(self):
        while True:
            try:
                if self.spd[0][0] == ' ' * 8 and len(self.sfd) == 0:
                    Printer('\n'*40,'{}{}'.format(' '*30,'YOU WIN!!!'))._printer_()
                    break
                pb = PyramidBoard(self.spd, self.sfd)
                Printer(pb.take_out_pyramid(), pb.take_out_spare_deck())._printer_()
                arg1 = Input('input card 1 and 2 or END to end the game, ENTER to flip a deck or rules to read the rules.\n\nCard 1: ')._input_()
                flag = GameCore(self.spd, arg1, self.sfd).get_condition()
                if arg1 == '':
                    self.sfd = GameCore(self.sfd).working_on_deck()
                    raise ValueError
                elif arg1.lower() == 'end':
                    break
                elif arg1.lower() == 'rules' or arg1.lower() == 'r':
                    Printer('\n\nTHE RULES OF SOLITAIRE PYRAMID (13)', Rules().show_rules())._printer_()
                if flag == False:
                    raise ValueError
                deck = GameCore(self.spd, arg1, self.sfd).kill_king()
                if deck[1] == True:
                    raise ValueError
                else:
                    arg2 = Input('Card 2: ')._input_()
                    flag = GameCore(self.spd, arg2, self.sfd).get_condition()
                    if flag == False:
                        raise ValueError
                    act = GameCore(self.spd, arg1, arg2, self.sfd)
                    act12 = act.kill_cards()
                    self.spd = act12[0]
                    self.sfd = act12[1]
            except ValueError:
                continue
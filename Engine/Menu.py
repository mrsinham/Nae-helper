__author__ = 'julien'
from Character.Creator import Creator as CharacterCreator

class Menu:

    def run(self):
        self.motd()
        iChoice = raw_input('Input the choice :')
        if ('1' == iChoice):
            oCreator = CharacterCreator()
            if False == oCreator.run():
                print 'Aborting character creation'
                self.run()
        elif ('4' == iChoice):
            print 'Bye bye'
            exit()
        else:
            self.run()

    def motd(self):
        print 'Welcome to Nae management program, what do you want to do ?'
        print '1 - Create character'
        print '2 - List characters'
        print '3 - Oppose character'
        print '4 - Exit'

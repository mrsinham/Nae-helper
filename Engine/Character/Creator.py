__author__ = 'julien'

from Entity.Character import Character

class Creator:

    def __init__(self):
        self.oCurrentCreator = Character()

    def run(self):
        bWantToBuildCharacter = self.askIfCharacterWanted()
        if (True != bWantToBuildCharacter):
            return False
        if (True != self.setFirstName()):
            return False
        if (True != self.setLastName()):
            return False
        if not self.setAge():
            return False


    def askIfCharacterWanted(self):
        print 'This creator will help you to build the characteristics, continue ?'
        bYesOrNot = raw_input('(y/n)')
        if bYesOrNot == 'y':
            return True
        elif bYesOrNot == 'n':
            return False
        else:
            return False

    def setFirstName(self):
        sFirstname = self.__getValue('Firstname')
        if False == sFirstname:
            return False
        self.oCurrentCreator.setFirstname(sFirstname)
        return True

    def setLastName(self):
        sLastname = self.__getValue('Lastname')
        if False == sLastname:
            return False
        self.oCurrentCreator.setLastname(sLastname)
        return True

    def setAge(self):
        sValue = self.__getValue('Age')
        sAge = int(sValue, 10);
        if (False == sAge):
            return False
        self.oCurrentCreator.setAge(sAge)
        return True

    def __getValue(self, sValueName):
        print 'Chose the '+sValueName
        sValue = raw_input('value : ')
        if (sValue == '') :
            return False
        return sValue
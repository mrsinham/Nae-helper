__author__ = 'julien'

class Character:

    def __init__(self):
        self.aAutorizedGender = ['m', 'f']
        self.aAutorizedChar = ['discernement', 'volonte', 'athletisme']
        self.aAutorizedLevels = ['vie', 'naergie']

        self.sLastName = None
        self.sFirstname = None
        self.iAge = None
        self.sGender = None
        self.dMainCharacteristics = {}
        self.dMainLevels = {}
        self.dSkillLevels = {}


    # Set a characteristic for the Entity
    def setCharacteristic(self, sCharacteristicName, mValue):

        if not self.aAutorizedChar.count(sCharacteristicName) :
            raise Exception('Unable to set a characteristic that is not in [' + ",".join(self.aAutorizedChar) + ']')
        self.dMainCharacteristics[sCharacteristicName] = mValue

    def setGender(self, sGender):
        if not self.aAutorizedGender.count(sGender):
            raise Exception('Unable to set an age that is not in [' + ",".join(self.aAutorizedGender) + ']')
        self.sGender = sGender

    def setAge(self, iAge):
        if not isinstance(iAge, int):
            raise Exception('Age must be int')
        self.iAge = iAge

    def setSkill(self, sSkillCode, iSkillPoint):
        if not isinstance(iSkillPoint, int) :
            raise Exception('Skill point must be integer')


    def setFirstname(self, sFirstname):
        self.sFirstname = sFirstname


    def setLastname(self, sLastname):
        self.sLastName = sLastname
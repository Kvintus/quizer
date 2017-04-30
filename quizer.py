class Quizer_obj(object):
    # init
    def __init__(self):
        super(Quizer_obj, self).__init__()
        # vytvaranie
        self.loadedSave = []

        # quizovanie
        self.totalQuesNum = 0
        self.quesRightPoints = 0
        self.loaded = []
        self.pageNum = 0

        # current
        self.currentPage = []
        self.currentAnswer = ""
        self.currentPageNum = 0

    # vytvaranie
    def addToList(self, listOdpov):
        for odpoved in listOdpov:
            self.loadedSave.append(odpoved + '\n')

    def writeToFile(self, cesta):
        print(self.loaded)
        hlavnaCesta = cesta[0] + cesta[1]
        with open(hlavnaCesta, 'w') as file:
            for item in self.loadedSave:
                file.write(item)

    # nacitavanie
    def loadList(self, cesta):
        hlavnaCesta = cesta[0]
        with open(hlavnaCesta, 'r') as file:
            self.loaded = file.readlines()
        self.totalQuesNum = len(self.loaded) / 5

    def setCurrentPageNum(self):
        self.currentPageNum = self.pageNum / 5

    def giveCurrentPageNum(self):
        self.setCurrentPageNum()
        return str(self.currentPageNum)[:1]  # 1, 2, 3, 4...

    def giveTotalQuesNum(self):
        return self.totalQuesNum

    def giveQuesRightPoint(self):
    	return self.quesRightPoints

    def giveCurrentAnswer(self):
        return self.currentAnswer

    def giveLoadedSave(self):
        return self.loadedSave

    def getPageList(self):
        bound = self.pageNum + 5
        chunked = []
        for item in range(self.pageNum, bound):
            chunked.append(self.loaded[item])
        self.pageNum += 5  # 0, 4, 9, 14...
        self.currentPage = chunked
        return chunked

    def setCurrentAnswer(self, theAnswer):
        self.currentAnswer = theAnswer
        '''
        for item in self.currentPage:
            if item[3:] == "spr":
                self.currentAnswer = item
            print(item)
        '''

    def compareAnswers(self, toCheck):
        if toCheck == self.currentAnswer:
            self.quesRightPoints += 1

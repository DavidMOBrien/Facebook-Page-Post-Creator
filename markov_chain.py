class MarkovChain():

    def __init__(self):
        self.startBank = {}
        self.wordBank = {[]}
    
    def addWord(self, word, follow):
        
        if word in wordBank:
            wordBank[word] = {}

        if follow in wordBank[word]:
            wordBank[word][follow] += 1
        else:
            wordBank[word][follow] = 1
    
    def addStart(self, word):
        if word in startBank:
            startBank[word] += 1
        else:
            startBank[word] = 1
    
    def train(self, aString):
        training = aString.split(' ')
        
        addStart(training[0])

        training.append('END_OF_STREAM')

        for i in len(training) - 1:
            addWord(training[i], training[i+1])

    def report(self):
        return self.wordBank

if __name__ == "__main__":
    mc = MarkovChain()
    mc.train('Does this work')
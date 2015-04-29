#lhy
#2015.4

import cPickle

class Analysis():
    def __init__(self):
        self.vectors = cPickle.load(open("vectors",'rb'))
        self.words = self.vectors.keys()
        self.scale = len(self.vectors[self.words[0]])
        self.dimensions = {}
        self.topWords = {}

    def dimension_analysis(self):
        for i in range(self.scale):
            self.dimensions[i] = {}
        for i in range(len(self.words)):
            vector = self.vectors[self.words[i]]
            for j in range(len(vector)):
                if vector[j] > 0:
                    self.dimensions[j][self.words[i]] = vector[j]
        for i in range(self.scale):
            self.topWords[i] = []
            dictionary = {}
            for (key,value) in self.dimensions[i].items():
                if value not in dictionary:
                    dictionary[value] = [key]
                else:
                    dictionary[value].append(key)
            index = dictionary.keys()
            index.sort()
            for j in range(len(index)):
                self.topWords[i].extend(dictionary[index[j]])
        cPickle.dump(self.topWords,open("top_words",'wb'))

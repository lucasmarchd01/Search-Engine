
import re
import AVLTreeMap as avl


class WebPageIndex:
    def __init__(self, file):
        self.filename = file
        self.filetext = open(file, "r").read().lower()
        self.wordindices = self.getWordIndices(self.filetext)
        self.wordcounts = self.getWordCounts(self.filetext)
        self.tree = self.getTree()

    def getWordCounts(self, str):
        """
        Returns a dictionary of key=word and val=word frequency.
        :param str:
        :return:
        """
        words = re.sub("[^\w' ]", '', str).split()
        wordfreq = {}
        for word, ind in self.wordindices.items():
            wordfreq[word] = len(ind)

        return wordfreq

    def getTree(self):
        """
        Construct the AVL Tree for a webpage.
        :return:
        """
        tree = avl.AVLTreeMap()
        for key, val in self.wordcounts.items():
            tree.root = tree.put(tree.root, key, val)
        return tree

    def getWordIndices(self, str):
        """
        Find the positions of words in the text file in a dictionary.
        :param str:
        :return:
        """
        words = re.sub("[^\w' ]", '', str).split()
        wordpositions = {}

        for word in words:
            indices = [i for i, x in enumerate(words) if x == word]
            if word not in wordpositions:
                wordpositions[word] = indices

        return wordpositions

    def getCount(self, s):
        """
        Return the wordcount of a word in a file.
        :param s:
        :return:
        """
        return self.wordcounts[s]


if __name__ == "__main__":
    wpi = WebPageIndex("data/doc1-arraylist.txt")
    print(wpi.getCount("the"))




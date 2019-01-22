'''
Created on 21-Dec-2017

@author: John
'''
import csv
import random
import math
class BayesClassifier(object):



    def __init__(self):
        pass
    
    def loadCsv(self,filename):
        lines = csv.reader(open(filename, "rb"))  #rb-"Read the file in Binary mode"
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
        return dataset

    def splitDataset(self,dataset, splitRatio):
        trainSize = int(len(dataset) * splitRatio)
        trainSet = []
        copy = list(dataset)
        while len(trainSet) < trainSize:
            index = random.randrange(len(copy))
            trainSet.append(copy.pop(index))
        return [trainSet, copy]
    
    def separateByClass(self,dataset):
        separated = {}
        for i in range(len(dataset)):
            vector = dataset[i]
            if (vector[-1] not in separated):
                separated[vector[-1]] = []
            separated[vector[-1]].append(vector)
        return separated
    
    def mean(self,numbers):
        return sum(numbers)/float(len(numbers))
    
    def stdev(self,numbers):
        avg = self.mean(numbers)
        variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
        return math.sqrt(variance)
    
    def summarize(self,dataset):
        summaries = [(self.mean(attribute), self.stdev(attribute)) for attribute in zip(*dataset)] #zip has come in handy for me is if you have an M by N array, and you want to look at columns instead of rows
        del summaries[-1]
        return summaries
    
    def summarizeByClass(self,dataset):
        separated = self.separateByClass(dataset)
        summaries = {}
        for classValue, instances in separated.iteritems():
            summaries[classValue] = self.summarize(instances)
        return summaries
    
    def calculateProbability(self,x, mean, stdev):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
    
    def calculateClassProbabilities(self,summaries, inputVector):
        probabilities = {}
        for classValue, classSummaries in summaries.iteritems():
            probabilities[classValue] = 1
            for i in range(len(classSummaries)):
                mean, stdev = classSummaries[i]
                x = inputVector[i]
                probabilities[classValue] *= self.calculateProbability(x, mean, stdev)
        return probabilities
                
    def predict(self,summaries, inputVector):
        probabilities = self.calculateClassProbabilities(summaries, inputVector)
        bestLabel, bestProb = None, -1
        for classValue, probability in probabilities.iteritems():
            if bestLabel is None or probability > bestProb:
                bestProb = probability
                bestLabel = classValue
        return bestLabel
    
    def getPredictions(self,summaries, testSet):
        predictions = []
        for i in range(len(testSet)):
            result = self.predict(summaries, testSet[i])
            predictions.append(result)
        return predictions
    
    def getAccuracy(self,testSet, predictions):
        correct = 0
        for i in range(len(testSet)):
            if testSet[i][-1] == predictions[i]:
                correct += 1
        return (correct/float(len(testSet))) * 100.0
    
    def main(self):
        #F:\Programs\Python Project\Sample1\src\pima-indians-diabetes.data.csv
        filename = 'F:\Programs\Python Project\Sample1\src\Output.csv'
        splitRatio = 0.67
        dataset = self.loadCsv(filename)
        trainingSet, testSet = self.splitDataset(dataset, splitRatio)
        print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
        # prepare model
        summaries = self.summarizeByClass(trainingSet)
        # test model
        predictions = self.getPredictions(summaries, testSet)
        accuracy = self.getAccuracy(testSet, predictions)
        var=accuracy
        print('Accuracy: {0}%').format(accuracy)
        return var
        
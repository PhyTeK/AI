import csv
import math
import random
import time
import sys,getopt

def loadCsv(filename):
    lines = csv.reader(open(filename))
    dataset = list(lines)

    data = []

    # Create categories
    for i in range(1,len(dataset)): # Jump over hearder
        value = float(dataset[i][2])

        if(value > 0.0):  # Reject uncorrect zero or negative values

            year = dataset[i][0][:4]

            category = dataset[i][0].replace(year,'').replace('-','').replace(':','')
            category = category.replace('00','').replace('+','').replace(' ','')
            
            data.append([year,category,value])

    return data

def cleartestSet(trainSet,testSet):
    for t in testSet:
        if not t in trainSet:
            del testSet[t]
    return [trainSet,testSet]

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def splitByYears(dataset, TestYear):
    trainSet = {}
    testSet = {}
    
    for year,instance,value in dataset:
        #print(year,instance,classValue)
        year = int(year)
        #instance = int(instance)
        #value = float(value)

        
        if year != TestYear:  # Change != to == for testing
            if instance not in trainSet:
                trainSet[instance] = []
            
            trainSet[instance].append(value)
        if year == TestYear:
            if instance not in testSet:
                testSet[instance] = []
            
            testSet[instance].append(value)
            
    return [trainSet, testSet]


def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[0] not in separated):
            separated[vector[0]] = []
        separated[vector[0]].append(vector[1])
    return separated

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    # Bessel corrected variance
    avg = mean(numbers)
    ln = len(numbers)
    if ln == 1:
        variance = 1 # Laplace bias
    else:
        variance = sum([pow(x-avg,2) for x in numbers])/float(ln - 1)
    return math.sqrt(variance)
    #return variance  # square of the unbiased sample variance 

def summarizePM(dataset):
    x = []
    for i in range(len(dataset)):
        x.append(dataset[i][1])
    summaries = (mean(x), stdev(x))
    del summaries[-1]
    return summaries


def summarize(dataset):
    
    summaries = (mean(dataset), stdev(dataset))
    #del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    #separated = separateByClass(dataset)
    #print(separated)
    summaries = {}
    for instance, classValues in dataset.items():
        summaries[instance] = (mean(classValues),stdev(classValues))
    return summaries


def calculateProbability(x, mean, stdev):
    x = float(x)
    stdev *= stdev # squared the variance
    if stdev != 0:
        exponent = math.exp(-(math.pow(x-mean,2)/(2*stdev)))
        return (1/(math.sqrt(2*math.pi)*stdev))*exponent
    else:
        return math.nan

def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}

    for classValue, classSummaries in summaries.items():
        #print(classValue,classSummaries,inputVector)

        probabilities[classValue] = 1
        mean, stdev = classSummaries
        try:
            x = inputVector[0]
        except:
            print('Error with inputVector', inputVector)
            exit(0)

        prob = calculateProbability(x, mean, stdev)
        
        if prob != math.nan:
            probabilities[classValue] *= prob

    return probabilities

def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    #print('\n',list(probabilities.items())[:20])
    #time.sleep(1)
    
    bestLabel, bestProb = None, -1

    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet):
    predictions = []
    i=0
    l=len(testSet)
    for k in testSet:
        print(" %\r",int(i/l*100 +1),end='')
        result = predict(summaries, testSet[k])
        #print(result)
        predictions.append(result)
        i += 1
    return predictions


def getAccuracy(testSet, predictions):
    correct = 0
    testSetDic = list(testSet.keys()) # Convert dict to list
     
    for i in range(len(testSet)):
        if testSetDic[i] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet)))*100.0

def writeResults(data,ref,outputfile):
    data = list(data)
    ref = list(ref)
    with open(outputfile,'w',newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            writer.writerow([data[i],ref[i]])
    return 'Done'


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)

    
    #filename = './data/se.csv'
    filename = inputfile
    TestYear = 2018
    print('Test year',TestYear)
    print('Read Datafile ...',end='')
    dataset = loadCsv(filename)
    print('Done')
    
    #trainingSet, testSet = splitDataset(dataset, splitRatio)
    trainingSet, testSet = splitByYears(dataset, TestYear)
    #print(trainingSet)

    #trainingSet,testSet = cleartestSet(trainingSet,testSet)
    
    print('Split {0} rows into train = {1} and test = {2} classes'.
          format(len(dataset),len(trainingSet),len(testSet)))
    print('Trainning ... ')
    #prepare model
    summaries = summarizeByClass(trainingSet)
    #print('sumaries: ',list(summaries.items())[:20])
    
    #test model
    #print(list(testSet)[:20])
    predictions = getPredictions(summaries, testSet)
    done = writeResults(predictions,testSet,outputfile)
    print(done)
    #predictions = list(testSet)
    #print(list(predictions)[:20])
          

    accuracy = getAccuracy(testSet, predictions)
    print('\nAccuracy: %3.2f%s'%(accuracy,'%'))


if __name__ == '__main__':
    main(sys.argv[1:])

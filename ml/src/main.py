from __future__ import division
from __future__ import print_function

import argparse
import re
import os
import cv2
import time
import editdistance
import tensorflow as tf
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
from vision import *
from nlp import *
from imageSeg import *
from warnings import filterwarnings
filterwarnings('ignore')

tf.get_logger().setLevel('ERROR')
class FilePaths:
    "filenames and paths to data"
    fnCharList = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/charList.txt'
    fnAccuracy = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/accuracy.txt'
    fnTrain = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/'
    # fnInfer = '../data/test.png'
    fnInfer = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/analyze.png'
    fnSegment = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/segments/'
    fnCorpus = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corpus.txt'
    fnWritten = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/written/'

def train(model, loader):
    "train NN"
    epoch = 0  # number of training epochs since start
    bestCharErrorRate = float('inf')  # best valdiation character error rate
    noImprovementSince = 0  # number of epochs no improvement of character error rate occured
    earlyStopping = 100  # stop training after this number of epochs without improvement
    while True:
        epoch += 1
        print('Epoch:', epoch)

        # train
        print('Train NN')
        loader.trainSet()
        while loader.hasNext():
            iterInfo = loader.getIteratorInfo()
            batch = loader.getNext()
            loss = model.trainBatch(batch)
            print('Batch:', iterInfo[0], '/', iterInfo[1], 'Loss:', loss)

        # validate
        charErrorRate = validate(model, loader)

        # if best validation accuracy so far, save model parameters
        if charErrorRate < bestCharErrorRate:
            print('Character error rate improved, save model')
            bestCharErrorRate = charErrorRate
            noImprovementSince = 0
            model.save()
            open(FilePaths.fnAccuracy, 'w').write(
                'Validation character error rate of saved model: %f%%' % (charErrorRate * 100.0))
                
        else:
            print('Character error rate not improved')
            noImprovementSince += 1

        # stop training if no more improvement in the last x epochs
        if noImprovementSince >= earlyStopping:
            print('No more improvement since %d epochs. Training stopped.' % earlyStopping)
            break


def validate(model, loader):
    "validate NN"
    print('Validate NN')
    loader.validationSet()
    numCharErr = 0
    numCharTotal = 0
    numWordOK = 0
    numWordTotal = 0
    while loader.hasNext():
        iterInfo = loader.getIteratorInfo()
        print('Batch:', iterInfo[0], '/', iterInfo[1])
        batch = loader.getNext()
        (recognized, _) = model.inferBatch(batch)
        #calculate runtime for each batch
        start = time.time()
        print('Runtime:', time.time() - start)
        #write it to a txt file
        f = open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/runtime.txt", "a")
        f.write(str(time.time() - start))
        f.write("\n")
        f.close()

        print('Ground truth -> Recognized')
        for i in range(len(recognized)):
            
            numWordOK += 1 if batch.gtTexts[i] == recognized[i] else 0
            numWordTotal += 1
            dist = editdistance.eval(recognized[i], batch.gtTexts[i])
            numCharErr += dist
            numCharTotal += len(batch.gtTexts[i])
            print('[OK]' if dist == 0 else '[ERR:%d]' % dist, '"' + batch.gtTexts[i] + '"', '->',
                  '"' + recognized[i] + '"')


    # print validation result
    charErrorRate = numCharErr / numCharTotal
    wordAccuracy = numWordOK / numWordTotal
    print('Character error rate: %f%%. Word accuracy: %f%%.' % (charErrorRate * 100.0, wordAccuracy * 100.0))
    return charErrorRate


def infer(model, fnImg):
    "recognize text in image provided by file path"
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    """ print('Recognized:', '"' + recognized[0] + '"')
    print('Probability:', probability[0]) """
    return recognized[0]

#function to store the recognised word onto a txt file
def storeText(recognized):
    f = open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/recognized.txt", "a")
    f.write(recognized)
    f.write("\n")
    f.close()

def storeVisionText(recognized):
    with open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/recognized.txt", "a") as f:
        for item in recognized:
            f.write("%s\n" % item)


def main():
    "main function"
    # optional command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', help='train the NN', action='store_true')
    parser.add_argument('--validate', help='validate the NN', action='store_true')
    parser.add_argument('--beamsearch', help='use beam search instead of best path decoding', action='store_true')
    parser.add_argument('--wordbeamsearch', help='use word beam search instead of best path decoding',
                        action='store_true')
    parser.add_argument('--dump', help='dump output of NN to CSV file(s)', action='store_true')
    
    parser.add_argument('--image', help='image to recognize text from', action='store_true' )
    parser.add_argument('--vision', help='recognizes text from images', action='store_true' )

    args = parser.parse_args()

    decoderType = DecoderType.BestPath
    if args.beamsearch:
        decoderType = DecoderType.BeamSearch
    elif args.wordbeamsearch:
        decoderType = DecoderType.WordBeamSearch

    # train or validate on IAM dataset
    if args.train or args.validate:
        # load training data, create TF model
        loader = DataLoader(FilePaths.fnTrain, Model.batchSize, Model.imgSize, Model.maxTextLen)

        # save characters of model for inference mode
        open(FilePaths.fnCharList, 'w').write(str().join(loader.charList))

        # save words contained in dataset into file
        open(FilePaths.fnCorpus, 'w').write(str(' ').join(loader.trainWords + loader.validationWords))

        # execute training or validation
        if args.train:
            model = Model(loader.charList, decoderType)
            train(model, loader)
        elif args.validate:
            model = Model(loader.charList, decoderType, mustRestore=True)
            validate(model, loader)

    # infer text from /data/segments folder
    elif args.image:        
        fnCharList = FilePaths.fnCharList
        #fnAccuracy = FilePaths.fnAccuracy
        fnInfer = FilePaths.fnInfer
        fnCorpus = FilePaths.fnCorpus
        fnSegment = FilePaths.fnSegment
        model = Model(open(fnCharList).read(), decoderType, mustRestore=True, dump=args.dump)
        images = []
        for file in os.listdir(fnSegment):
            if file.endswith(".png"):
                images.append(file)

        for image in images:
            fnImg = os.path.join(fnSegment, image)
            print(fnImg)
            # load trained model
            recognized = infer(model, fnImg)
            storeText(recognized)
            print('Recognized:', '"' + recognized + '"')
            print('----------------------------------------')

    elif args.vision:
        fnCharList = FilePaths.fnCharList
        #fnAccuracy = FilePaths.fnAccuracy
        fnSegment = FilePaths.fnSegment
        fnWritten = FilePaths.fnWritten
        images = []
        for file in os.listdir(fnWritten):
            if file.endswith(".jpg"):
                images.append(file)

        for image in images:
            fnImg = os.path.join(fnWritten, image)
            print(fnImg)
            recognized = image_to_text(fnImg)
            storeVisionText(recognized)
            spellChecker()
    # infer text on test image
    else:
        fnCharList = FilePaths.fnCharList
        #fnAccuracy = FilePaths.fnAccuracy
        fnSegment = FilePaths.fnSegment
        fnWritten = FilePaths.fnWritten
        images = []
        for file in os.listdir(fnWritten):
            if file.endswith(".jpg"):
                images.append(file)

        for image in images:
            fnImg = os.path.join(fnWritten, image)
            #imageSeg(fnImg)
            print(fnImg)
            recognized = image_to_text(fnImg)
            storeVisionText(recognized)
            spellChecker()

        print("Model ran successfully!")
main()
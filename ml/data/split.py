import glob 
import os
import pandas as pd 

'''
words.txt format -
format: a01-000u-00-00 ok 154 1 408 768 27 51 AT A

    a01-000u-00-00  -> word id for line 00 in form a01-000u
    ok              -> result of word segmentation
                           ok: word was correctly
                           er: segmentation of word can be bad

    154             -> graylevel to binarize the line containing this word
    1               -> number of components for this word
    408 768 27 51   -> bounding box around this word in x,y,w,h format
    AT              -> the grammatical tag for this word, see the
                       file tagset.txt for an explanation
    A               -> the transcription for this word

'''
#split the words.txt file with the following format
# a01-000u-00-00 ok 154 1 408 768 27 51 AT A becomes a01-000u-00-00, ok, 154, 1, 408 768 27 51, AT, A
# column 1 - word id
# column 2 - result of word segmentation
# column 3 - graylevel to binarize the line containing this word
# column 4 - number of components for this word
# column 5 - bounding box around this word in x,y,w,h format
# column 6 - the grammatical tag for this word
# column 7 - the transcription for this word

#add column names to the csv file
def add_column_names(csv_file):
    df = pd.read_csv(csv_file)
    df.columns = ['word_id', 'result', 'graylevel', 'number_of_components', 'bounding_box', 'grammatical_tag', 'transcription']
    df.to_csv(csv_file, index=False)

#split the words.txt file into csv files
def split_words_file(words_file):
    for line in open(words_file):
        line = line.strip()
        line = line.split(' ')
        word_id = line[0]
        result = line[1]
        graylevel = line[2]
        number_of_components = line[3]
        bounding_box = line[4] + ' ' + line[5] + ' ' + line[6] + ' ' + line[7]
        grammatical_tag = line[8]
        transcription = line[9]
        csv_file = '/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/words.csv'
        with open(csv_file, 'a') as f:
            f.write(word_id + ',' + result + ',' + graylevel + ',' + number_of_components + ',' + bounding_box + ',' + grammatical_tag + ',' + transcription + ' \n') 
        add_column_names(csv_file)


#main
def main():
    words_file = 'words copy.txt'
    split_words_file(words_file)

main()

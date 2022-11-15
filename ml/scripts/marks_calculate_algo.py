
#NLP output txt file
import csv

import numpy as np

NLP_file_output= "/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt"

NLP_list = []

#store NLP output in array
while True:
    with open(NLP_file_output, 'r+') as f:
        #if file is empty
        if f.read(1):
            f.seek(0)
            for line in f:
                NLP_list.append(line)
        else:
            print("NLP file is empty")
            f.write(" ")
            break



#print(NLP_list)

NLP_array = np.asarray(NLP_list)

#for i in range(0,len(NLP_array)):
    #print(NLP_array[i])


def normal_weightage(NLP_array):
    #normal_matches = []
    normal_matches_found =[]
    normal_weightage_score =0
    for obj1 in range(0,len(NLP_array)):
        for keyword_present2 in range(0,len(keyword_array)):
            #print(keyword_array)
            if(keyword_array[keyword_present2]==NLP_array[obj1]):
                normal_matches_found.append(keyword_array[keyword_present2])
                #print(normal_matches_found)
                normal_weightage_score+=keyword_weightage_array[keyword_present2]
    normal_matches_found_no_duplicates = set(normal_matches_found)
    #print(normal_matches_found_no_duplicates)
    #print(normal_weightage_score)
    normal_weightage_score_list=[]
    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/records.csv', 'a', encoding='UTF8') as f2:
    # create the csv writer
        writer = csv.writer(f2)
        writer.writerow(normal_weightage_score_list)
    normal_weightage_score_list.append(normal_weightage_score)
    return normal_weightage_score_list
    

#normal_weightage(NLP_array)

def view_array(arr):
    for i in arr:
        print(i)


def custom_weightage(NLP_array):
    custom_matches_found =[]
    custom_weightage_score =0
    for obj1 in range(0,len(NLP_array)):
        for keyword_present2 in range(0,len(custom_keyword_array)):
            #print(keyword_array)
            if(custom_keyword_array[keyword_present2]==NLP_array[obj1]):
                custom_matches_found.append(custom_keyword_array[keyword_present2])
                #print(normal_matches_found)
                custom_weightage_score+=custom_keyword_weightage_array[keyword_present2]
    custom_matches_found_no_duplicates = set(custom_matches_found)
    #print(custom_matches_found_no_duplicates)
    #print(custom_weightage_score)
    custom_weightage_score_list=[]
    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/records.csv', 'a', encoding='UTF8') as f2:
    # create the csv writer
        writer = csv.writer(f2)
        writer.writerow(custom_weightage_score_list)
    custom_weightage_score_list.append(custom_weightage_score)
    return custom_weightage_score_list

#normal_weightage(NLP_array)


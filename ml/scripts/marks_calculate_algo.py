
#NLP output txt file
import numpy as np

NLP_file_output= ""

NLP_list = []

with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt','r') as file:  
    for line in file:     
        for word in line.split():         
            NLP_list.append(word)

#print(NLP_list)

NLP_array = np.asarray(NLP_list)

'''
for i in range(0,len(NLP_array)):
    print(NLP_array[i])
'''


def normal_weightage(NLP_array):
    keyword_weightage = 0
    n=int(input('Enter the number of keywords: '))
    keyword_normal_matches =[]
    matches_found =[]
    for i in range(0,n):
        keyword = input('Enter the keyword: ')
        keyword_normal_matches.append(keyword)

    matches_array = np.asarray(keyword_normal_matches)


    for obj in range(0,len(NLP_array)):
        for keyword_present in range(0,len(matches_array)):
            if(matches_array[keyword_present]==NLP_array[obj]):
                matches_found.append(matches_array[keyword_present])
                keyword_weightage+=10
    matches_found_no_duplicates = set(matches_found)
    
    print(keyword_weightage)
    #print(keyword_normal_matches)
    #print(matches_found_no_duplicates)


#normal_weightage(NLP_array)

def view_array(arr):
    for i in arr:
        print(i)


def custom_weightage(NLP_array):
    n_keywords=int(input('Enter the number of keywords: '))
    custom_matches = []
    keyword_list =[]
    keyword_weightage_list =[]
    for i in range(0,n_keywords):
        keyword = input('Enter the keyword: ')
        keyword_list.append(keyword)
        keyword_weightage = int(input('Enter the weightage associated with the keyword: '))
        keyword_weightage_list.append(keyword_weightage)

    keyword_array = np.asarray(keyword_list)
    keyword_weightage_array = np.asarray(keyword_weightage_list)

    #view_array(keyword_array)
    #view_array(keyword_weightage_list)

    weightage_score =0
    custom_matches_found =[]

    for obj1 in range(0,len(NLP_array)):
        for keyword_present2 in range(0,len(keyword_array)):
            #print(keyword_array)
            if(keyword_array[keyword_present2]==NLP_array[obj1]):
                custom_matches_found.append(keyword_array[keyword_present2])
                #print(custom_matches_found)
                weightage_score+=keyword_weightage_array[keyword_present2]
                

    custom_matches_found_no_duplicates = set(custom_matches_found)
    #print(custom_matches_found_no_duplicates)
    print(weightage_score)


#custom_weightage(NLP_array)



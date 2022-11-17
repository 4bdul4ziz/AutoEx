#NLP output txt file
import numpy as np
import csv

NLP_file_output= "/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt"

NLP_list = []

with open(NLP_file_output,'r') as file:  
    for line in file:     
        for word in line.split():         
            NLP_list.append(word)

#print(NLP_list)

NLP_array = np.asarray(NLP_list)

#for i in range(0,len(NLP_array)):
    #print(NLP_array[i])


def normal_weightage(NLP_array):
    keyword_weightage = 0  #initial keyword weightage
    n=int(input('Enter the number of keywords: '))
    keyword_normal_matches =[]
    matches_found =[]
    for i in range(0,n):
        keyword = input('Enter the keyword: ')
        with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/examinerList.txt','a') as file:  
            file.write(keyword+'\n')
        keyword_normal_matches.append(keyword)

    matches_array = np.asarray(keyword_normal_matches)


    for obj in range(0,len(NLP_array)):
        for keyword_present in range(0,len(matches_array)):
            if(matches_array[keyword_present]==NLP_array[obj]):
                matches_found.append(matches_array[keyword_present])
                keyword_weightage+=10
    matches_found_no_duplicates = set(matches_found)

    keyword_weightage_list=[]
    keyword_weightage_list.append(keyword_weightage)

    #print(keyword_weightage)

    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/keywordMatches.txt','a') as file:  
        file.write(str(matches_found_no_duplicates))     #writes the matches onto the keyword_matches file
    
    fields = ['marks']
    rows = [keyword_weightage_list]
    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/records.csv', 'a') as file:
        writer = csv.writer(file)
        #writer.writerow(fields)
        writer.writerows(rows)  #appends the final keyword weightage 
    
    return keyword_weightage


def custom_weightage(NLP_array):
    n_keywords=int(input('Enter the number of keywords: '))
    #custom_matches = []
    keyword_list =[]
    keyword_weightage_list =[]
    for i in range(0,n_keywords):
        keyword = input('Enter the keyword: ')
        with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/examinerList.txt','a') as file:  
            file.write(keyword+'\n')
        keyword_list.append(keyword)
        keyword_weightage = int(input('Enter the weightage associated with the keyword: '))
        with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/customWeights.txt','w') as file:  
            file.write(str(keyword_weightage))
        keyword_weightage_list.append(keyword_weightage)

    keyword_array = np.asarray(keyword_list)
    keyword_weightage_array = np.asarray(keyword_weightage_list)

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
    
    weightage_score_list=[]
    weightage_score_list.append(weightage_score)

    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/keywordMatches.txt','a') as file:  
        file.write(str(custom_matches_found_no_duplicates))     #writes the matches onto the keyword_matches file
    
    fields = ['marks']
    rows = [weightage_score_list]
    with open('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/records.csv', 'a') as file:
        writer = csv.writer(file)
        #writer.writerow(fields)
        writer.writerows(rows)          #appends the final keyword weightage 
    return weightage_score

#custom_weightage(NLP_array)

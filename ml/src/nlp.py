from textblob import TextBlob
 

def spellChecker():
    #open recognized text file
    with open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/recognized.txt", "r") as f:
        text = f.read()

    #convert text to blob
    blob = TextBlob(text)

    #correct spelling
    corrected = blob.correct()

    # write corrected text with one word on each line to a file
    with open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt", "w") as f:
        for word in corrected.words:
            f.write(word + " ");
            f.close();


        """  with open("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt", "w") as f:
        f.write(str(corrected)) """
    
#spellChecker()
    

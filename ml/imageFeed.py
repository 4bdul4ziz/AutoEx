#this function is used to get the images from /data/segments and put them into a list and runs the python main.py --image <path> where <path> will be the images in the list
import os 

def getImages():

    #get all the images in the folder
    images = []
    for file in os.listdir("ml/data/segments/"):
        if file.endswith(".png"):
            images.append(file)
    #print(images)
    #run the python main.py --image <path> where <path> will be the images in the list
    for image in images:
        
        os.system("python main.py --image ml/data/segments/" + image)
        print("python main.py --image data/segments/" + image)


getImages()



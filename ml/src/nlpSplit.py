
def yeet(textFile):
    with open(textFile, 'r') as f:
        lines = f.readlines()
        newLines = []
        for line in lines:
            line = line.strip()
            line = line.split(' ')
            if len(line) > 1:
                for word in line:
                    with open('recognized_split.txt', 'a') as f:
                        f.write(word + ' \n')
            else:
                with open('recognized_split.txt', 'a') as f:
                    f.write(line[0] + ' \n')
yeet("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/recognized.txt")
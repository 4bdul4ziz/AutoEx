# Automated Examiner
## A tool to automate the process of correcting a handwritten answer sheet.

This tool uses handwritten text detection trained using CNN, RNN and CTC loss function. The model is trained on the IAM dataset. The model is trained using tensorflow and keras. 

The model is used to extract the text from the image and the extracted text is sent to a NLP pipeline to correct the spelling errors. The corrected text is then compared with the correct answer key. The score is calculated and displayed.

We use Apple's Vision Kit interfaced with Python using the objective c wrapper to detect and store the handwritten text data on top of the trained model to increase the accuracy of the text detected to ensure proper gradings.

The tool is built using Python and the GUI is built using R Shiny.

## Installation
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Navigate to the ml/src directory and run `python main.py`
4. Drop the image of the answer sheet in the ml/data/writings directory
5. To run the GUI, navigate to the R directory and run `AutoEx_interface.R`

## Usage
1. The GUI will open up. Click on the "Browse" button to select the image of the answer sheet.
2. Choose the method of awarding marks, custom weightage or default weightage for the keywords.
3. Click on the "Submit" button to get the score.
4. The score will be displayed on the screen. 
5. The class average score will be displayed on the screen, alongside the score of the student.

This project is a part of the course project for the courses CSE4082, CSE3105 & CSE3505 at VIT University, Chennai.

## Contributors
1. Abdul Aziz
2. Samik Saraswat
3. Roselyn




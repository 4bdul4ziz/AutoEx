
#UI R - interface [ui.R] frontend
#Server function [server.R] backend
#shinyApp function [fuses both ui and server]

#flow of i/o
#input -> ui -> server ->[process analyze data]
#output <- ui <- server <- [processed data]

library(shiny)
library(shinythemes)
library(reticulate)
#import python modules
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/main.py")
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/scripts/marks_calculate_algo.py")

ui <- fluidPage(theme = shinytheme("slate"),
                titlePanel("Auto EX"),
                sidebarLayout(position = "left",
                  sidebarPanel(
                    tags$h3("Normal Weightage "),
                    textInput("keyword_input", "Enter the keywords:", ""),
                    actionButton("normal_button","Normal weightage calculate"),
                    textOutput("button_works"),
                    tags$h3("Custom Weightage "),
                    textInput("keyword_input", "Enter the keywords:", ""),
                    textInput("weightage_input","enter the weightage associated with the custom keywords: "),
                    actionButton("custom_button","Custom weightage calculate"),
                    textOutput("button_works_custom")
                    
                  ),
                  
                  mainPanel(
                    h3("NLP pipeline output Text"),
                    #h4("The keywords matched and the weightage associated is: "),
                    #textInput("string_data","Enter the string: "),
                    textOutput("string_data"),
                    h3("The examiner entered keywords list: "),
                    textOutput("examiner_list")
                    #uiOutput(outputId = "my_ui")
                    
                    
                  )
                ),
                sidebarLayout(
                  sidebarPanel(
                    tags$b("Model Execution"),
                    actionButton("model_run","Execute Model"),
                    textOutput("model_output")
                  ),
                  mainPanel()
                ),
                sidebarLayout(
                  sidebarPanel(
                    tags$h4("Marks calcuated based on weightage are: "),
                    textOutput("marks_output")
                  ),
                  mainPanel()
                ),
                sidebarLayout(
                  sidebarPanel(
                    fileInput("image_dummy", "Select the scanned image file",
                              multiple = FALSE,
                              accept = c('image/png',
                                         ".jpg")),
                    
                    # Horizontal line ----
                    tags$hr()
                  ),  
                  mainPanel(
                  
                  )
                #actionButton(parameter<-script, label, icon = NULL, width = NULL, ...). 
                #here we will be having the executing button for executing the script of the model and 
                #output will be the text file of handwritten words
                
                #actionButton(function<-weightage calculation, label, icon = NULL, width = NULL, ...)
                )
    
          
)





server <- function(input, output) {
  
  observeEvent(input$normal_button, {
    marks <- normal_weightage(NLP_array) #here instead of function1 we will we calling normal_weightage 
    output$button_works <-renderText({
      paste( marks )  #saves the weightage [o/p of the function and renders as text and prints on interface]
    })
    
  })
  
  observeEvent(input$custom_button, {
    marks2 <- custom_weightage(NLP_array) #here instead of function1 we will we calling custom_weightage 
    output$button_works_custom <-renderText({
      paste( marks2 )  #saves the weightage [o/p of the function and renders as text and prints on interface]
    })
    
  })
  
  observeEvent(input$model_run, {
    model_works<- main() #calling the main.py for model
    output$model_output <-renderText({
      paste( model_works )  #add a print statement in the main function that "model ran successfully"
    })
    
  })
  
  observeEvent(input$image_dummy, {
      inFile <- input$image_dummy
      if (is.null(inFile))
        return()
      img<-file.copy(inFile$datapath, file.path("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/written/", inFile$name) ) #here is the directory you want the scanned image in
  })
  
  
  #checking the image by printing onto the interface
 
  
  output$my_ui<-renderUI({
      img(src=img,height = '300px')
  })
  
  
  
  reading_data <-read.delim("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt",              # TXT data file indicated as string or full path to the file
                            header = FALSE,    # Whether to display the header (TRUE) or not (FALSE)
                            sep = "\n",          # Separator of the columns of the file
                            dec = ".")         # Character used to separate decimals of the numbers in the file
  output$string_data <- renderText({
    paste(reading_data) #functions 
  })
  
  list_of_keywords_by_examiner <-read.table("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/examinerList.txt",
                             header= FALSE,
                             sep= "",
                             dec =".")
  output$examiner_list <-renderText({
    paste(list_of_keywords_by_examiner)
  })
  
    
} # server


# Create Shiny object
shinyApp(ui = ui, server = server)
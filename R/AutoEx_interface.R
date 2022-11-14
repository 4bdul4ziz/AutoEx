
#UI R - interface [ui.R] frontend
#Server function [server.R] backend
#shinyApp function [fuses both ui and server]

#flow of i/o
#input -> ui -> server ->[process analyze data]
#output <- ui <- server <- [processed data]

library(shiny)
library(shinythemes)
source_python("/Users/samik/Desktop/Programming/AutoEx/test.py")

ui <- fluidPage(theme = shinytheme("cerulean"),
                titlePanel("Auto EX"),
                sidebarLayout(position = "left",
                  sidebarPanel(
                    tags$h3("Keyword  Input:"),
                    textInput("keyword_input", "Enter the keywords:", "")
                  ),
                  
                  mainPanel(
                    h3("NLP pipeline output Text"),
                    #h4("The keywords matched and the weightage associated is: "),
                    #textInput("string_data","Enter the string: "),
                    textOutput("string_data"),
                    h3("The examiner entered keywords list: "),
                    textOutput("examiner_list"),
                    
                  )
                ),
                sidebarLayout(
                  sidebarPanel(
                    tags$b("Keyword Count"),
                    textOutput("keyword_output")
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
                    fileInput("input_txt", "Choose the txt file",
                              multiple = FALSE,
                              accept = c("text/plain",
                                         ".txt", "space")),
                    
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
  
  output$keyword_output <- renderText({
    paste( keywords ) #functions 
  })
  output$marks_output <- renderText({
    marks <-function1()
    paste( marks ) #functions 
  })
  #functions using algorithm that will award the marks based on examiners choice 
  #under development
  keyword_count <- function(string_data) {
    
  return(keywords)
  }
  
  calculate_marks <-function(keywords){
    
    return(marks)
  }
  
  

  
  
  reading_data <-read.table("input_txt.txt",              # TXT data file indicated as string or full path to the file
                            header = FALSE,    # Whether to display the header (TRUE) or not (FALSE)
                            sep = "",          # Separator of the columns of the file
                            dec = ".")         # Character used to separate decimals of the numbers in the file
  output$string_data <- renderText({
    paste(reading_data) #functions 
  })
  
  list_of_keywords_by_examiner <-read.table("examiner_list.txt",
                             header= FALSE,
                             sep= "",
                             dec =".")
  output$examiner_list <-renderText({
    paste(list_of_keywords_by_examiner)
  })
  
    
} # server


# Create Shiny object
shinyApp(ui = ui, server = server)
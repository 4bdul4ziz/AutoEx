#R interface lmao ded

library(shiny)
library(shinythemes)
library(reticulate)

source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/main.py")
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/new_marks_algo.py")
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/record_generator.py")

ui <- fluidPage(theme = shinytheme("slate"),
  titlePanel("AutoEx"),
  sidebarLayout(position = "left",
    sidebarPanel(
      tags$h4("Buttons for weightage calculation: "),
      tags$h2("Normal Weightage "),
      actionButton("normal_weightage_button","Normal weightage calculate"),
      textOutput("normal_weightage_print"),
      tags$h2("Custom Weightage "),
      actionButton("custom_weightage_button","Custom weightage calculate"),
      textOutput("custom_weightage_print")
    ),
    
    mainPanel(
      h4("NLP pipeline output text is: "),
      textOutput("NLP_output"),
      h4("The user/examiner entered keywords are: "),
      textOutput("keyword_examiner_list"),
      #img(src = "image.png", height=512, width=512, align="centre") #trying to add image but failed?
      
    )
    
  
),
  sidebarLayout(
    sidebarPanel(
      tags$b("Model Execution"),
      actionButton("model_run","Execute Model"),
      textOutput("model_output"),
      tags$b("Statistical data generation(csv)"),
      actionButton("records_generate","Generates csv file"),
      textOutput("csv_output")
    ),
    mainPanel()
  ),
  sidebarLayout(
    sidebarPanel(
      fileInput("image_dummy", "Select the scanned image file",
                multiple = FALSE,
                accept = c('image/png',
                           ".jpg")),
      
      tags$hr()
    ),  
    mainPanel()
  )

)

server <- function(input, output) {
  
  observeEvent(input$normal_weightage_button, {
    normal_weightage_score <- normal_weightage(NLP_array) #normal weightage function mapped
    output$normal_weightage_print <-renderText({
      paste( normal_weightage_score ) 
    })
    
  })
  
  observeEvent(input$custom_weightage_button, {
    custom_weightage_score <- custom_weightage(NLP_array) #custom weightage function mapped 
    output$custom_weightage_print <-renderText({
      paste(custom_weightage_score)  
    })
    
  })
  
  
  observeEvent(input$model_run, {
    model_works<- main() #calling the main.py for model
    output$model_output <-renderText({
      paste(model_works)  #add a print statement in the main function that "model ran successfully"
    })
    
  })
  
  
  observeEvent(input$records_generate, {
    csv_done<- generating_csv() 
    output$csv_output <-renderText({
      paste(csv_done)  
    })
    
  })
  
  
  observeEvent(input$image_dummy, {
    inFile <- input$image_dummy
    if (is.null(inFile))
      return()
    img<-file.copy(inFile$datapath, 
                   file.path("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/written/", 
                   inFile$name) ) #here is the directory you want the scanned image in
    
    output$testimage <- renderImage({
      list(
        src = inFile,
        filetype = "image/jpeg",
        alt = "This is a image"
      )
    })
  })
  
  
  NLP_file_read <- read.delim("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/corrected.txt", header = TRUE, sep = "\n")
  output$NLP_output <- renderText({
    #li <- list(NLP_file_read)
    paste(toString(NLP_file_read)) 
  })
  
  
  examiner_list <- read.delim("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/examinerList.txt", header = TRUE, sep = "\n")
  output$keyword_examiner_list<-renderText({
    paste(examiner_list)
  })
  
  
  
}

shinyApp(ui = ui, server = server)
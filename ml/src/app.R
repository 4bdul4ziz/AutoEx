#R interface lmao ded

library(shiny)
library(shinythemes)
library(reticulate)
library(ggplot2)
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/main.py")
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/new_marks_algo.py")
source_python("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/src/record_generator.py")


data <- read.csv("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/judgement.csv", header = TRUE, sep = ",")
classAvg <- aggregate(marks ~ StudentID, data, mean)
sGrade <- quantile(classAvg$marks, 0.25)
aGrade <- quantile(classAvg$marks, 0.75)
grade <- c("S", "A", "B", "C", "D", "E")
gradeCount <- c(sum(classAvg$marks > sGrade), sum(classAvg$marks > aGrade), sum(classAvg$marks > 60), sum(classAvg$marks > 50), sum(classAvg$marks > 40), sum(classAvg$marks > 30))
model <- lm(marks ~ StudentID, data)



ui <- fluidPage(theme = shinytheme("slate"),
  titlePanel("AutoEx"),
  sidebarLayout(position = "left",
    sidebarPanel(
      tags$h4("Buttons for weightage calculation: "),
      tags$h2("Normal Weightage "),
      actionButton("normal_weightage_button","Normal weightage calculate"),
      tags$br(),
      textOutput("normal_weightage_print"),
      tags$br(),
      tags$h2("Custom Weightage "),
      actionButton("custom_weightage_button","Custom weightage calculate"),
      tags$br(),
      textOutput("custom_weightage_print")
    ),
    
    mainPanel(
      h4("NLP pipeline output text is: "),
      textOutput("NLP_output"),
      tags$br(),
      h4("The user/examiner entered keywords are: "),
      textOutput("keyword_examiner_list"),
      tags$br()
      #img(src = "image.png", height=512, width=512, align="centre") #trying to add image but failed?
      
    )
    
  
),
  sidebarLayout(
    sidebarPanel(
      tags$b("Model Execution"),
      actionButton("model_run","Execute Model"),
      textOutput("model_output"),
      tags$br(),
      tags$b("Statistical data generation(csv)"),
      actionButton("records_generate","Generates csv file"),
      textOutput("csv_output"),
      tags$br()
    ),
    mainPanel()
  ),
  sidebarLayout(
    sidebarPanel(
      fileInput("image_dummy", "Select the scanned image file",
                multiple = FALSE,
                accept = c('image/png',
                           ".jpg")),
      
      tags$hr(),
      actionButton("scatter_line","Generate Scatter+Line Plot"),
      tags$hr(),
      actionButton("sd_plt","Generate Standard Deviation"),
      tags$hr(),
      actionButton("pie_plt","Generate Pie Plot"),
      tags$hr(),
      actionButton("lm_plt","Generate Linear Model")
      
    ),  
    mainPanel(
      tags$h2("Statistical Analysis of Data based on Model: "),
      tags$br(),
      plotOutput("plot1"),
      plotOutput("plot2"),
      plotOutput("plot4"),
      plotOutput("plot5")
    )
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
    model_works<- function_main() #calling the main.py for model
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
                   file.path("/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/written", 
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
  
  
  
  #for scatter+line plot on button press
  scatter_line_plot <- eventReactive(input$scatter_line, {
    ggplot(data, aes(x = StudentID, y = marks)) +
      geom_point() +
      geom_line(colour="red")+
      labs(title = "Scatter+Line Plot", x = "Number of Students", y = "Relative weightage")
  })
  
  output$plot1<-renderPlot({
    scatter_line_plot()
  })
  
  #for sd plot on button press
  standard_deviation_plot<- eventReactive(input$sd_plt, {
    ggplot(data, aes(x = StudentID, y = marks)) +
      geom_point() +
      geom_errorbar(aes(ymin = marks - sd(marks), ymax = marks + sd(marks)), width = 0.2) +
      labs(title = "Standard Deviation ", x = "Number of Students", y = "Relative weightage")
  })
  
  output$plot2 <- renderPlot({
    standard_deviation_plot()
  })
  
  #for pie plot on button press
  pie_plot <- eventReactive(input$pie_plt, {
    pie(gradeCount, labels = grade, col = rainbow(length(grade)))
  })
  
  output$plot4 <- renderPlot({
    pie_plot()
  })
  
  
  #for linear model plot on button press
  lm_plot <-eventReactive(input$lm_plt, {
    ggplot(data, aes(x = StudentID, y = marks)) +
      geom_point() +
      geom_smooth(method = "lm", se = TRUE) +
      labs(title = "Linear Model Plot", x = "Number of Students", y = "Relative Weightage")
  })
  
  output$plot5 <- renderPlot({
    lm_plot()
  })
  

}

shinyApp(ui = ui, server = server)
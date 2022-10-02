library(shiny)
library(shinythemes)

ui <- fluidPage(theme = shinytheme("cerulean"),
                titlePanel("Auto EX"),
                sidebarLayout(position = "left",
                  sidebarPanel(
                    tags$h3("Keyword  Input:"),
                    textInput("keyword_input", "Enter the keywords:", "")
                  ),
                  
                  mainPanel(
                    h1("Selected Text"),
                    #h4("The keywords matched and the weightage associated is: "),
                    #textInput("string_data","Enter the string: "),
                    textOutput("string_data")
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
                  mainPanel()
                  
                )
    
          
)

server <- function(input, output) {
  
  output$keyword_output <- renderText({
    paste( keywords ) #functions 
  })
  output$marks_output <- renderText({
    paste( marks ) #functions 
  })
  
  keyword_count <- function(string_data) {
    
  return(keywords)
  }
  
  calculate_marks <-function(keywords){
    
    return(marks)
  }
  reading_data <-read.table("testing.txt",              # TXT data file indicated as string or full path to the file
                            header = FALSE,    # Whether to display the header (TRUE) or not (FALSE)
                            sep = "",          # Separator of the columns of the file
                            dec = ".")         # Character used to separate decimals of the numbers in the file
  output$string_data <- renderText({
    paste(reading_data) #functions 
  })

    
} # server


# Create Shiny object
shinyApp(ui = ui, server = server)
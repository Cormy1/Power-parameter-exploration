library(shiny)
library(ggplot2)
library(stats)

# Function to calculate required sample size
calculate_sample_size <- function(effect_size, alpha, power) {
  power.t.test(power = power, delta = effect_size, sig.level = alpha, alternative = "two.sided")$n
}

# Define the UI
ui <- fluidPage(
  titlePanel("Sample Size vs. Effect Size"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("effect_size", "Effect Size", min = 0.005, max = 2, value = 0.3, step = 0.005),
      sliderInput("alpha", "Significance Level", min = 0, max = 0.1, value = 0.05, step = 0.01),
      sliderInput("power", "Power", min = 0, max = 1, value = 0.8, step = 0.01),
      textOutput("sample_size_text")  # Add text box output
    ),
    mainPanel(
      plotOutput("sample_size_plot")
    )
  )
)

# Define the server logic
server <- function(input, output) {
  output$sample_size_plot <- renderPlot({
    effect_sizes <- seq(0.005, 2, 0.005)
    sample_sizes <- sapply(effect_sizes, function(es) calculate_sample_size(es, input$alpha, input$power))
    
    df <- data.frame(Effect_Size = effect_sizes, Sample_Size = sample_sizes)
    
    ggplot(df, aes(x = Sample_Size, y = Effect_Size)) +
      geom_line(color = "mediumorchid") +
      geom_point(data = df[df$Effect_Size == input$effect_size, ], aes(x = Sample_Size, y = Effect_Size), color = "midnightblue") +
      geom_vline(xintercept = df[df$Effect_Size == input$effect_size, "Sample_Size"], linetype = "dashed", color = "slateblue") +
      geom_hline(yintercept = df[df$Effect_Size == input$effect_size, "Effect_Size"], linetype = "dashed", color = "slateblue") +
      xlim(0, 500) +
      xlab("Sample Size") +
      ylab("Effect Size") +
      ggtitle(paste("Sample size vs. effect size for significance", input$alpha, "and power", input$power))
  })
  
  output$sample_size_text <- renderText({
    paste("Selected Sample Size:", calculate_sample_size(input$effect_size, input$alpha, input$power))
  })
}

# Run the Shiny app
shinyApp(ui = ui, server = server)

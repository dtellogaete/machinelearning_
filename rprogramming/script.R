# Import library
library(readr)
library(dplyr)

# Import dataset
dataset <- read_csv("hw1_data.csv")
str(dataset)

subdata <- dataset %>%
          filter(Ozone > 31 & Temp > 90)

mean(subdata$Solar.R)


month6 <- dataset %>%
          filter(Month == 6 )

mean(month6$Temp)


#----------------------------------

month5 <- dataset %>%
          filter(Month == 5 )
max(month5$Ozone, na.rm =  TRUE)

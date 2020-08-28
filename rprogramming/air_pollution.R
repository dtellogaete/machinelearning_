print(R.version.string)

#Importar librerías
library(readr)
library(dplyr)

#Funcion `pollutantmean`
pollutantmean <- function(directory, pollutant, id = 1:332){
  files <- list.files(directory)
  dir <- paste(directory, "/", "001.csv", sep = "")
  
  poll_vector <- list()
  for (i in id){
    dataset <- read_csv(paste(directory, "/", files[i], sep = ""))
    poll_vector[length(poll_vector)+1] <-dataset[pollutant]
  }
  poll_vector <- unlist(poll_vector)
  avg <- mean(poll_vector, na.rm = TRUE)
  return(avg)
}


#Función complete

complete <- function(directory, id = 1:332){
  files <- list.files(directory)
  nobs <- list()
  for (i in id){
    dataset <- read_csv(paste(directory, "/", files[i], sep = ""))
    nobs[length(nobs)+1] <- sum(!is.na(dataset['sulfate']))
  }
  nobs <- unlist(nobs)
  df <- data.frame(id, nobs)
  return(df)
}

#Funcion corr

corr <- function(directory, threshold = 0){
  files <- list.files(directory)
  df <- complete(directory)
  df_set <- df %>%
    filter(nobs>threshold)
  ids <- df_set$id
  
  cor_value <- list()
  for (i in ids){
    dataset <- read_csv(paste(directory, "/", files[i], sep = ""))
    dataset <- dataset[!is.na(dataset$sulfate),]
    cor_value[length(cor_value)+1] <- cor(dataset["sulfate"], 
                                           dataset["nitrate"])
  }
  cor_value <- unlist(cor_value)
  return(cor_value)
}


#-----------------------------------------------------

cr <- corr("specdata")                
cr <- sort(cr)   
RNGversion("3.5.1")
set.seed(868)                
out <- round(cr[sample(length(cr), 5)], 4)
print(out)

cr <- corr("specdata", 129)                
cr <- sort(cr)                
n <- length(cr)    
RNGversion("3.5.1")
set.seed(197)                
out <- c(n, round(cr[sample(n, 5)], 4))
print(out)


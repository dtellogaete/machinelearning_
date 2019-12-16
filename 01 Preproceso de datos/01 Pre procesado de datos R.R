# Plantilla para el Pre Procesado de datos
# Importar el dataset
dataset = read.csv('01 Preproceso de datos/Data.csv')
#dateset = dataset[, 2:3]

# Trataemiento de los valores NA

dataset$Age = ifelse(is.na(dataset$Age), mean(dataset$Age, na.rm = TRUE),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary), mean(dataset$Salary, na.rm = TRUE),
                        dataset$Salary)

dataset

# Codificar las variables categóricas

dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1))

# Dividir los datos en conjunto de entrenamiento y conjunto de test

library(caTools)

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])






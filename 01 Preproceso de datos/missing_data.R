# Plantilla para el Pre Procesado de datos -Datos faltantes
# Importar el dataset
dataset = read.csv('01 Preproceso de datos/Data.csv')

# Trataemiento de los valores NA

dataset$Age = ifelse(is.na(dataset$Age), mean(dataset$Age, na.rm = TRUE),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary), mean(dataset$Salary, na.rm = TRUE),
                        dataset$Salary)
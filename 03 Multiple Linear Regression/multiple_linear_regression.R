# Regresión Lineal Múltiple

# Importar el dataset
dataset = read.csv('03 Multiple Linear Regression/50_Startups.csv')

# Codificar las variables categóricas
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1,2,3))

# Dividir los datos en conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de Regresion Lineal Múltiple con el Conjunto de Entrenamiento
regression = lm(formula= Profit ~ .,
                data = training_set)

# Predecir los resultadols con el conjunto de testing
y_pred = predict(regression, newdata = testing_set)

# Construir un módelo óptimo con la elimación hacia atrás
SL = 0.05
regression = lm(formula= Profit ~ R.D.Spend + Administration + Marketing.Spend
                +State,
                data = dataset)
summary(regression)

regression = lm(formula= Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula= Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula= Profit ~ R.D.Spend,
                data = dataset)
summary(regression)





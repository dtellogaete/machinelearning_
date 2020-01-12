# SVR

# Importar el dataset

dataset = read.csv('05 Support Vector Regression/Position_Salaries.csv')
dataset = dataset[, 2:3]

#Ajustar SVR con el conjunto de datos
#install.packages("e1071")
library(e1071)
regression = svm(formula = Salary ~ .,
                 data = dataset,
                 type = "eps-regression",
                 kernel = "radial")

#Prediccion de nuevos resultadops con SVR 
y_pred = predict(regression, newdata = data.frame(Level= 6.5))

# Visualización del modelo SVR
#install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicción (Modelo de Regresión)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")

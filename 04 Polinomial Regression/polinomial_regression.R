# Regresion Polinomica

# Importar el dataset
dataset = read.csv('04 Polinomial Regression/Position_Salaries.csv')
dataset = dataset[, 2:3]

# Ajustar modelo de regresión lineal con el conjunto de datos
lin_reg = lm(formula = Salary~.,
             data = dataset)

# Ajustar modelo de regresión polinómica con el conjunto de datos
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

poly_reg = lm(formula = Salary~.,
              data = dataset)

# Visualización del modelo lineal
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") + 
  geom_line(aes(x =dataset$Level, 
                y =predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Predicción lineal del suelo en función del nivel del empleado")+
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")

# Visualización del modelo polinómico
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") + 
  geom_line(aes(x =dataset$Level, 
                y =predict(poly_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Predicción lineal del suelo en función del nivel del empleado")+
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")

# Prediccion de nuevos resultados con Regresion Lineal 
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Prediccion de nuevos resultados con Regresión Polinómica
y_pred = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5^2,
                                                Level3 = 6.5^3,
                                                Level4 = 6.5^4))




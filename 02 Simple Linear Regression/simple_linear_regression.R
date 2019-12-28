# Regresión Lineal Simple

# Importar el dataset
dataset = read.csv('02 Simple Linear Regression/Salary_Data.csv')

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# -SplitRatio indica eel numero de elementos que son seleccionados para training

library(caTools)

set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de rls con el conjunto de entrenamiento
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# Predecir resultados con el conjunto de test
# - newdata los nombres deben llamarse igual que en regressor
y_pred = predict(regressor, newdata = testing_set)

# Visualización de los resultados en el conjunto de entrenamiento
library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,
                 y=training_set$Salary),
             colour = "red")+
  geom_line(aes(x=training_set$YearsExperience,
                y=predict(regressor, newdata = training_set)),
            colour = "blue")+
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")+
  xlab("Años de Experiencia")+
  ylab("Sueldo 2")

# Visualización de los resultados en el conjuntod de testing
ggplot()+
  geom_point(aes(x=testing_set$YearsExperience,
                 y=testing_set$Salary),
             colour = "red")+
  geom_line(aes(x=testing_set$YearsExperience,
                y=predict(regressor, newdata = testing_set)),
            colour = "blue")+
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")+
  xlab("Años de Experiencia")+
  ylab("Sueldo 2")





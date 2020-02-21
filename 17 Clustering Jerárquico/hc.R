# Clustering Jerárquico

# Importar los datos del centro comercial
dataset = read.csv("Mall_Customers.csv")
X = dataset[,4:5]

# Utilizar el dendrograma para encontrar el número óptimo de clusters
dendogram = hclust(dist(X, method = "euclidean"),
                   method = "ward.D")
plot(dendogram,
     main = "Dendrograma",
     xlab = "Clientes del centro comercial",
     ylab = "Distancia Euclidea")

# Ajustar el clustering jerárquico a nuestro dataset
hc = hclust(dist(X, method = "euclidean"),
                   method = "ward.D")
y_hc = cutree(hc, k = 5)

# Visualizar los clusteres
#install.packages("cluster")
library(cluster)
clusplot(X,
         y_hc,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = "Clustering de clientes",
         xlab = "Ingresos anuales",
         ylab = "Puntuación (1-100)")
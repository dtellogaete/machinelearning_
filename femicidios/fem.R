# Importar dataset

fem2019 <- read.csv("fem2019.csv", header = TRUE, sep = ";")

fem2020 <- read.csv("fem2020.csv", header = TRUE, sep = ";")

fem2019 <- data.frame(fem2019)

# Import librerias
library(dplyr)
library(lubridate)

# Agrupar por mes
fem2019$month <- (month(dmy(fem2019$Fecha)))
fem2020$month <- month(dmy(fem2020$Fecha))

# Serie de tiempo

fem2019_month <- fem2019 %>%
                group_by(month) %>%
                summarise(total = n())

fem2020_month <- fem2020 %>%
                group_by(month) %>%
                summarise(total = n())

fem2019_month$year <- 2019
fem2020_month$year <- 2020
                

femtotal <- data.frame(seq(1,20))
femtotal$femicidios <- c(fem2019_month$total, 
                         fem2020_month$total)
femtotal$year <- c(fem2019_month$year, fem2020_month$year)
femtotal$month <- c(fem2019_month$month, fem2020_month$month)
femtotal$month <- month.abb[femtotal$month
femtotal$year <- as.factor(femtotal$year)

#Grafica

library(ggplot2)

ggplot(femtotal, aes(x = month, y = femicidios, color = year))+
  geom_line(size = 1) +
  geom_point()+
  scale_x_continuous(name = "", 1:12)+
  ggtitle("Feminicidios por Año - Chile") +
  xlab("Mes") +
  ylab("Cantidad") +
  labs(color = "Año")


  

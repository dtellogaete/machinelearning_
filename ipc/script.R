#Import libraries

library(quantmod)
library(dplyr)


#Función para extraer los datos 
extract_data <- function(shares,index, date){
  data = getSymbols(index, 
                    from=date,
                    src="yahoo",
                    auto.assign = F)[,6]
  nrowShare = length(data)
  index_date = index(data)
  dataset = as.data.frame(matrix(nrow = nrowShare, ncol = length(shares)))
  colnames(dataset) = shares
  dataset$date = index_date
  
  iniCol = 1
  for (i in shares){
    dataset[iniCol]<-as.numeric(getSymbols(i, from=date,src="yahoo",auto.assign = F)[,6])
    iniCol = iniCol+1
  }
  
  return(dataset)
}

#IPC
ipc<- c('RA.MX', 'KIMBERA.MX', 'ALPEKA.MX', 'TLEVISACPO.MX', 'CUERVO.MX', 'PINFRA.MX', 'BOLSAA.MX',
        'GRUMAB.MX', 'AMXL.MX', 'CEMEXCPO.MX', 'GCARSOA1.MX', 'GMEXICOB.MX', 'AC.MX', 'ASURB.MX', 'MEGACPO.MX', 'BSMXB.MX',
        'LABB.MX', 'GENTERA.MX', 'BIMBOA.MX', 'GFNORTEO.MX', 'GAPB.MX', 'IENOVA.MX',
        'BBAJIOO.MX', 'GCC.MX', 'ALSEA.MX','OMAB.MX')

#Descargar los datos
ipc_data<- extract_data(ipc,'^MXX', '2020-01-01')

#Media movil Exponencial

ipc_ra <- as.data.frame(as.numeric(EMA(ipc_data$RA.MX)))
colnames(ipc_ra) <- 'moving_average'
ipc_ra$moving_average[is.na(ipc_ra$moving_average)]<-0
ipc_ra$price <- ipc_data$RA.MX
ipc_ra$date <- ipc_data$date


write.csv(ipc_ra, file = "ra.csv")

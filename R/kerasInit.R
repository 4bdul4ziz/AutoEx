install.packages(c("keras", "tensorflow"))

install.packages("devtools")

remotes::install_github("rstudio/reticulate@fix/conda-activate")


library(devtools)
devtools::install_github("rstudio/keras", dependencies = TRUE)
devtools::install_github("rstudio/tensorflow", dependencies = TRUE)

library(keras)
library(tensorflow)

install_keras()
install_tensorflow()

library(keras)
library(tensorflow)
library(reticulate)
mnist <- dataset_mnist()
x_train <- mnist$train$x
y_train <- mnist$train$y
x_test <- mnist$test$x
y_test <- mnist$test$y

# reshape
x_train <- x_train / 255
x_test <- x_test / 255

dim(x_train) <- c(60000, 28, 28, 1)
dim(x_test) <- c(10000, 28, 28, 1)

y_train <- to_categorical(y_train, 10)
y_test <- to_categorical(y_test, 10)

model <- keras_model_sequential()
model %>%
  layer_conv_2d(kernel_size = c(3, 3), filter = 32, activation = "relu") %>%
  layer_conv_2d(kernel_size = c(3, 3), filter = 64, activation = "relu") %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_dropout(dropout = 0.25) %>%
  layer_flatten() %>%
  layer_dense(units = 128, activation = "relu") %>%
  layer_dropout(dropout = 0.5) %>%
  layer_dense(units = 10, activation = "softmax")



model %>% compile(
  loss = "categorical_crossentropy",
  optimizer = optimizer_adadelta(),
  metrics = c("accuracy")
)

history <- model %>% fit(
  x_train, y_train,
  epochs = 12, batch_size = 128,
  validation_split = 0.2
)

model %>% evaluate(x_test, y_test)

library(png)
pic3 <- list.files("/Users/abdul/Desktop/Programming/R Programs/AutoEx")
setwd("/Users/abdul/Desktop/Programming/R Programs/AutoEx")
my_image <- readPNG(pic3[1])
my_image <- my_image[, , 1]

img_mat <- t(apply(img_mat, 2, rev))
image(img_mat, col = gray((0:255) / 255))

img_mat <- my_image[, , 1]
hand <- as.vector(t(img_mat))
Xt <- hand
Xt <- array_reshape(Xt, c(1, 28, 28, 1))
model %>% predict_classes(Xt)




# R Solution
library(caret)
training <- read.csv("har_train.csv", na.strings = c("NA", ""))
test <- read.csv("har_validate.csv", na.strings = c("NA", ""))

# Train Naive Bayes using klaR
library(klaR)

# Train
nb_mod <- NaiveBayes(classe ~ ., data=training, fL=1, usekernel = T) . # with kernel and laplace correction = 1

# Predict
pred <- suppressWarnings(predict(nb_mod, test))

# Confusion Matrix
tab <- table(pred$class, test$classe)
caret::confusionMatrix(tab)  # Computes the accuracy metrics for all individual classes.

# Plot the Confusion Matrix
library(ggplot2)
test$pred <- pred$class
ggplot(test, aes(classe, pred, color = classe)) +
  geom_jitter(width = 0.3, height = 0.3, size=1) +
  labs(title="Confusion Matrix", 
       subtitle="Predicted vs. Observed from HAR dataset", 
       y="Predicted", 
       x="Truth", 
       caption="machinelearningplus.com")
rm(list=ls())
library(Hmisc)
data <- read.csv("C:/Users/emery/Desktop/Data Analysis/R/data/COVID19_line_list_data.csv")
describe(data)

#clean up death column
data$death_dummy <- as.integer(data$death != 0) #convert into binary where 1 represents death and 0 represents no death

#death rate
sum(data$death_dummy) / nrow(data)

#Is age related to death rate?
death = subset(data, death_dummy == 1)
alive = subset(data, death_dummy == 0)
mean(death$age, na.rm = TRUE)
mean(alive$age, na.rm = TRUE)
t.test(alive$age, death$age, alternative = "two.sided", conf.level = 0.95)
# p-value < 2.2e-16 < 0.05, so the null hypothesis is rejected.

#Does death rate statistically significant regarding gender?
male = subset(data, gender == "male")
female = subset(data, gender == "female")
mean(male$death_dummy)
mean(female$death_dummy)
t.test(male$death_dummy, female$death_dummy, alternative = "two.sided", conf.level = 0.95)
# p-value = 0.002105 < 0.05, so the null hypothesis is rejected.

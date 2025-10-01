library(dplyr)
library(tidytuesdayR)
library(ggplot2)
#Analysis
tuesdata <- tidytuesdayR::tt_load('2024-09-10')
college_admissions <- tuesdata$college_admissions
View(college_admissions)
sum_grouped_college_admissions <- college_admissions %>%
  group_by(par_income_lab) %>%
  summarise(
    count=n(),
    mean_par_income_bin=mean(par_income_bin, na.rm=TRUE),
    median_par_income_bin=median(par_income_bin, na.rm=TRUE),
    mean_attend_level=mean(attend_level, na.rm=TRUE))
View(sum_grouped_college_admissions)
#Plot
ggplot(sum_grouped_college_admissions, aes(x = par_income_lab, y = mean_par_income_bin, color = par_income_lab)) + 
  geom_point()

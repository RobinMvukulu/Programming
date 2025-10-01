library(dplyr)
library(tidytuesdayR)
library(ggplot2)
#Analysis
tuesdata <- tidytuesdayR::tt_load("2024-01-09")
canada_births_1991_2022 <- tuesdata$canada_births_1991_2022
nhl_player_births <- tuesdata$nhl_player_births
nhl_rosters <- tuesdata$nhl_rosters
nhl_teams <- tuesdata$nhl_teams
View(canada_births_1991_2022)
View(nhl_player_births)
View(nhl_rosters)
View(nhl_teams)
glimpse(nhl_rosters)

#1
filtered_canada_births_2019_2022 <- canada_births_1991_2022 |>
  filter((year >= 2019 & year <= 2022) 
         & births >= "32000") %>%
  group_by(month) %>%
  summarise(
    count= n()
  )
View(filtered_canada_births_2019_2022)
ggplot(filtered_canada_births_2019_2022, aes(x=month, y=count)) +
         geom_col()

#2
library(lubridate) #To retrieve only the year from a date
filtered_nhl_player_births <- nhl_player_births |>
  filter(birth_country != "CAN" &
           (last_name == "Liam" | last_name == "James" | last_name == "William")) %>%
  group_by(birth_country) %>%
  summarise(
    country=birth_country,
    count=n(),
    id=player_id,
    year=year(birth_date),
    name=last_name
  )
View(filtered_nhl_player_births)

#3
library(stringr)
filtered_nhl_rosters <- nhl_rosters |>
  filter((position_type == "goalies" | position_type == "defensemen") &
           str_starts(team_code, "M")) %>%
  group_by(team_code) %>%
  summarise(
    count=n()
  )
View(filtered_nhl_rosters)
ggplot(filtered_nhl_rosters, aes(x=team_code, y=count)) +
  geom_col()

#4
filtered_nhl_teams <- nhl_teams |>
  filter(str_starts(full_name, "T")) %>%
  group_by(team_code)
View(filtered_nhl_teams)

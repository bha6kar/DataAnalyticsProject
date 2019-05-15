# Set working dir to source dir
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

# Set libPaths.
.libPaths("~\\R\\3.5")

# Load required packages.
library(janitor)
library(lubridate)
library(hms)
library(tidyr)
library(stringr)
library(readr)
library(openxlsx)
library(forcats)
library(RcppRoll)
library(dplyr)
library(tibble)
library(exploratory)

# Set OAuth token.
exploratory::setTokenInfo("twitter", as.environment(list(user_id = "789090380", screen_name = "Onyx", oauth_token = "490554898-Phjhdjf6gr89jk3n4u38n86tHyyd7", oauth_token_secret = "avcr78tbix7634bhrxn783o4LSLGnj3c78", consumer_sc = "dhgsjfhisdlbyfoiyxie67f7yf86et7")))

# Steps to produce the output
data <- exploratory::select_columns(exploratory::clean_data_frame(exploratory::getTwitter(searchString = '#aapl', n = 20000, lang = '', lastNDays = 20, tokenFileId = '', includeRts = FALSE, withSentiment = TRUE)),"created_at","text","sentiment") %>% readr::type_convert() %>%
  filter(sentiment != 0) %>%
  mutate(date = parse_character(created_at)) %>%
  select(date, everything()) %>%
  separate(date, into = c("date_1", "date"), sep = "\\s+", convert = TRUE) %>%
  select(-date) %>%
  rename(date = date_1) %>%
  select(-created_at)

print (data)
write.csv(data, "twitter.csv", fileEncoding="UTF-8")

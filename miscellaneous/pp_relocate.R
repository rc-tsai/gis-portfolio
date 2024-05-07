
# scenario 2
before_job <- c(4, 19, 5)
before_pop <- c(38, 8, 50)


# scenario 1
before_job <- c(5, 2, 10)
before_pop <- c(17, 2, 2)

# scenario (rounding up in STEP 3)
before_job <- c(4, 19, 5)
before_pop <- c(40, 8, 50)

df <- data.frame(before_job, before_pop)

# STEP 1
# dissimilarity before people relocate
df$before_pop_job_dissimilarity <- (df$before_pop / sum(df$before_pop, na.rm=TRUE)) - 
  (df$before_job / sum(df$before_job, na.rm = TRUE))

# STEP 2
# number of people need to relocated from each area
#(positive value = number of pp need to move out from that area, vice versa)
df$pp_need_relocate <- round(sum(df$before_pop, na.rm=TRUE)*df$before_pop_job_dissimilarity)

# STEP 3
# number of people after relocation
df$after_pop <- df$before_pop - df$pp_need_relocate

# dissimilarity after people relocate
df$after_job_pop_dissimilarity <-  (df$after_pop / sum(df$after_pop, na.rm=TRUE)) - 
  (df$before_job / sum(df$before_job, na.rm = TRUE))

# before and after job-pop ratio
df$before_job_pop_ratio <- df$before_job / df$before_pop
df$after_job_pop_ratio <- df$before_job / df$after_pop

# ideal job-pop ratio
df$ideal <- sum(df$before_job) / sum(df$before_pop)



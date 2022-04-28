#!/bin/bash
# 
# This script is used to generate basic reports on system utilization based
# on data held in the metadata database.

# Database and output settings
DB_NAME=cadre_meta
## Put the full path to the reports directory here
## and include trailing slash.
CSV_REPORTS_DIRECTORY="/var/lib/postgresql/reports/"
WRITE_CSV=false

# 
USER_COUNT_BY_INSTITUTION_QUERY="SELECT institution, COUNT(id) AS user_count FROM user_login GROUP BY institution ORDER BY institution ASC"
JOB_COUNT_BY_USER_QUERY="SELECT user_login.name, user_login.id AS user_id, COUNT(user_login.id) AS user_job_count FROM user_login JOIN user_job ON user_login.id = user_job.user_id GROUP BY user_login.id ORDER BY user_login.name ASC"

if [[ "$WRITE_CSV" != "true" ]]; then
   # Count number of users at each institution
   echo "--------------------------------"
   echo "User count by institution"
   echo "--------------------------------"
   psql --dbname ${DB_NAME} --command "${USER_COUNT_BY_INSTITUTION_QUERY}"
   echo
   echo

   # Job counts per user
   echo "--------------------------------"
   echo "Job count by user"
   echo "--------------------------------"
   psql --dbname ${DB_NAME} --command "${JOB_COUNT_BY_USER_QUERY}"
   echo
   echo
else
   # Job counts per user
   psql --dbname ${DB_NAME} --command "Copy(${USER_COUNT_BY_INSTITUTION_QUERY}) To '${CSV_REPORTS_DIRECTORY}/user_count_by_institution.csv' With CSV DELIMITER ',' HEADER;"

   # Count number of users at each institution
   psql --dbname ${DB_NAME} --command "Copy(${JOB_COUNT_BY_USER_QUERY}) To '${CSV_REPORTS_DIRECTORY}/job_count_by_user.csv' With CSV DELIMITER ',' HEADER;"
fi


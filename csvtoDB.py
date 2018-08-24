# portCSV.sql
mysql -uroot -p --local-infile

LOAD DATA LOCAL INFILE "file.csv"
INTO TABLE db.table
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
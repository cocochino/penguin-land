# MySQL Workbench Keyboard Shortcut
# Ctrl-Enter -> Run Current SQL selection
# Shift-Ctrl-Enter -> Run All or Selection

# More about working with MySQL

USE world;
SHOW tables;

# To see details of tables in the database
SHOW table status;

# To reverse engineer tables
SHOW CREATE TABLE city;
#Results - showing data type
CREATE TABLE `city` (
   `ID` int NOT NULL AUTO_INCREMENT,
   `Name` char(35) NOT NULL DEFAULT '',
   `CountryCode` char(3) NOT NULL DEFAULT '',
   `District` char(20) NOT NULL DEFAULT '',
   `Population` int DEFAULT NULL,
   PRIMARY KEY (`ID`)
 ) ENGINE=InnoDB AUTO_INCREMENT=4080 DEFAULT CHARSET=utf8mb3
 ;

#
# Numerics
#
 
# Differences in precision - decimal vs fload. Check the results of the following calculation
USE scratch;
SELECT * from numerics;
SELECT da+db, fa+fb from numerics;
SELECT da+db=0.3 from numerics; # This is true. Use Dicimal for currency
SELECT fa+fb=0.3 from numerics; # This is false!
  
#
# DATE and TIME
#

# Sanity check of time format;
SELECT NOW();

# Show time related system variables
SHOW variables LIKE '%time_zone%';

#Checking UTC
SELECT utc_timestamp();

# Setting UTC as default
SET time_zone = '+00:00';
SELECT NOW();

# Setting local timezone
SET time_zone = 'SYSTEM';
SELECT NOW();

#
# String
# 

# CHAR or VARCHAR, BINARY, VARBINARY, BLOB, TEXT. 

CREATE TABLE test (
  id INT UNSIGNED UNIQUE AUTO_INCREMENT PRIMARY KEY,
  a ENUM( 'Pablo', 'Henri', 'Jackson' )
);
 
INSERT INTO test ( a ) VALUES ( 'Pablo' );
INSERT INTO test ( a ) VALUES ( 'Henri' );
INSERT INTO test ( a ) VALUES ( 'Jackson' );
INSERT INTO test ( a ) VALUES ( 1 );
INSERT INTO test ( a ) VALUES ( 2 );
INSERT INTO test ( a ) VALUES ( 3 );
SELECT * FROM test;
INSERT INTO test ( a ) VALUES ( 4 );
DROP TABLE IF EXISTS test;

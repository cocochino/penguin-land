# MySQL Workbench Keyboard Shortcut
# Ctrl-Enter -> Run Current SQL selection
# Shift-Ctrl-Enter -> Run All or Selection

#
# NAVIGATING Database
#

# USE -> select database
USE world;

# SHOW -> List tables 
SHOW TABLES;

# Display column names and data types
DESCRIBE album;

#
# CRUD
#

# SELECT statement with ORDER BY
SELECT * FROM Country ORDER BY Name;

# Giving the selected column alias
SELECT Name AS Country, Code AS ISO, Region, Population AS Pop from Country ORDER BY Code;

# Counting rows with WHERE Clause
SELECT COUNT(*) FROM Country WHERE Population > 1000000 AND Continent = 'Asia';

#
#
# Now switch database
USE scratch;

# INSERT statement with INSERT... VALUES...
INSERT INTO Customer (name, city, state) VALUES ('Poodle Dog', 'New York', 'NY' );

# Update using UPDATE... SET ...
UPDATE Customer SET address ='123 Posh Street, Apt #99' WHERE id = 4;
SELECT * FROM Customer WHERE name LIKE 'Po%';


# DELETING records - Basically change from SELECT to DELETE
SELECT * from test;
DELETE from test where b = 'another';

# DROPping table
DROP TABLE test;
# or
DROP TABLE IF EXISTS test;


#
# Basic JOIN
#

# JOIN
USE album;
SELECT a.artist AS Artist, 
a.title AS Album, 
t.track_number AS 'Track Num',
t.title AS Track, t.duration AS Seconds
FROM album AS a
JOIN track AS t ON a.id = t.album_id
ORDER BY a.artist, a.title, t.track_number;


#
# Boolean
# Any non-0 result is treated as TRUE

#False
SELECT 0 = 1;
SELECT (9 > 2) IS NOT TRUE;
SELECT 1 XOR 1; # One side of operation is TRUE
SELECT 1 IS NOT TRUE; 
SELECT 1 IS NULL;
SELECT 0 IS NULL;
SELECT '' IS NULL;
SELECT 5 IN (1, 3, 7);

#true
SELECT (9 - 2) = 7;
SELECT (5 - 2) IS TRUE;
SELECT (9 > 2) IS TRUE;
SELECT 1 AND 1; #TRUE
SELECT 1 OR 1; #TRUE
SELECT 1 OR 0; #TRUE or FALSE = TRUE
SELECT 1 XOR 0; # One side of operation is TRUE
SELECT 1 IS NOT NULL;
SELECT 0 IS NOT NULL;
SELECT '' IS NOT NULL;
SELECT 5 IN (1, 3, 5, 7);

# Arithmatic
# PEDMUS - Parenthesis, Exp, Div, Multi, 
SELECT 5/3;
SELECT 5 DIV 3; # Division
SELECT 5 % 3; # Modulus
SELECT 5 MOD 3; # Modulus
SELECT 5/0; # This is NULL

#
# CASE
#
USE scratch;

#Test table
CREATE TABLE booltest (a INTEGER, b INTEGER);
INSERT INTO booltest values (1, 0);
SELECT * from booltest;
#Checking column's true/false with CASE: Using the column name in condition
SELECT
	CASE WHEN a < 5 THEN 'true' ELSE 'false' END AS boolA,
    CASE WHEN b > 5 THEN 'true' ELSE 'false' END AS boolB
    FROM booltest
;    

#Checking column's true/false with CASE : Using the column name in CASE name
SELECT
	CASE a WHEN 1 THEN 'true' ELSE 'false' END AS boolA,
    CASE b WHEN 1 THEN 'true' ELSE 'false' END AS boolB
    FROM booltest
;    


#
# IF
#
SELECT IF(a < 5, 'Yes!!!', 'Nope') FROM booltest;
SELECT IF(b < 0, 'true', 'false') FROM booltest;
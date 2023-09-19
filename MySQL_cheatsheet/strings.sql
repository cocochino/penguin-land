#
# STRINGS
# 

use world;

# underscore '_' is the single character wildcard. The following specifies 'a' in the 2nd character
SELECT name from country WHERE name LIKE '_a%' ORDER BY name;

#String Comparison. The following example list country names that sorts lower than or equal to France
SELECT name from country WHERE STRCMP(name, 'France') <= 0 ORDER BY name;

#
# Regular Expressoins !!!!!
#

# RegEx LIKE = RLIKE
# End with 'y'
SELECT name from country WHERE name RLIKE 'y$';

#name has x or y that is followed by a or i
SELECT name from country WHERE name RLIKE '[xy][ai]';


# Doesn't use standard string concatination
# CONCAT() function with comma
SELECT concat('This', ' and', ' that ', 42);

#Numeric conversion
SELECT 32742;
SELECT HEX(32742); # HEX
SELECT OCT(32742); # Octet
SELECT BIN(32742); # binary
SELECT CONV(32742, 10, 16); # Convert from decimal to Hex
SELECT CONV('7FE6', 16, 10); # Convert from Hex to decimal

# Trimming
SELECT '    Mooshu    ';
SELECT TRIM('    Mooshu    ');
SELECT CONCAT(':', TRIM('    Mooshu    '), ':'); # This makes trimmed space clear
SELECT CONCAT(':', LTRIM('    Mooshu    '), ':'); # This makes trimmed space clear
SELECT CONCAT(':', TRIM('y' FROM 'yyyy  Mooshu    '), ':'); # This makes trimmed space clear

# Padding
SELECT LPAD('MOOSHU', 15, '*');
SELECT RPAD('MOOSHU', 10, '*');

# Converting case
#Lower case - LCASE
use scratch;
SELECT * FROM customer;

SELECT LCASE(name) FROM customer;

#Making Title Case
# Convert 1 char from the the 1st char to Upper case, then the chars after 2nd to lower case then concatinate
SELECT CONCAT( UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2)) ) FROM customer;

# SUBSTRINGS
#
SELECT SUBSTR('Dogs are good.', -5); # return the last 5 chars
SELECT SUBSTRING_INDEX('Dogs are good.', ' ', 1); # return up to the first space char

#SOUNDEX - Sounds like!
SELECT SOUNDEX('duck'), SOUNDEX('muck');
SELECT SOUNDEX('luck'), SOUNDEX('lack');

SELECT 'miyagi' sounds like 'miyako', 'miyagi' sounds like 'minato';

SELECT TRUE || CONCAT('Hello', 'world');

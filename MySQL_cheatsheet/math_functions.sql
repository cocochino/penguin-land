/* 
Standard comment uses '--' followed by a space
Also MySQL supports C style comment / *  * / and #
Math functions
from LinkedIn.com/Learn
*/

SELECT ABS(-11.55); # Anwwer is 11.55

SELECT CEILING(7.5); # Answer is 8

SELECT floor(7.5); # Answer is 7

SELECT ROUND(7.5); # Answer is 8

SELECT truncate(13.789, 1); # Answer is 13.7
SELECT truncate(13.789, 2); # Answer is 13.78
SELECT truncate(13.789, -1); # Answer is 10, because negative number indicate the lest side 13 -> 10

-- Use pi and decimal numbers to control the output
SELECT pi(); # '3.141593'
SELECT pi() + 0.0000000000; # 3.1415926536

SELECT POWER(4, 2); # 4^2 = 16
SELECT SQRT(16); # 4
# OR... quarter root
SELECT POWER(16, 1/4); # 2

# Random number
SELECT RAND();
SELECT RAND(34567); # with seed


# Trig!
SELECT SIN(2);
SELECT COS(PI());
SELECT TAN(PI());

# Logarithms
SELECT LOG(10, 100);
SELECT log10(1000);
SELECT LOG(2, 12334656);

#Degrees - When would I use this??
SELECT radians(180); # This is PI
SELECT degrees(PI()); # This is 180

SELECT EXP(4);
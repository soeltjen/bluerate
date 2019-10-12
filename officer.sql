/*
-- Query: SELECT * FROM officerrate.`officer table`
LIMIT 0, 1000

-- Date: 2019-10-12 14:10
*/

CREATE TABLE officers (
	badge integer,
	first char(64),
	last char(64),
	city char(64),
	stars float,
	profileid integer,
	primary key (profileid)
);


INSERT INTO officers (`badge`,`first`,`last`,`city`,`stars`,`profileid`) VALUES (123456,'john','smith','minneapolis',3,0);
INSERT INTO officers (`badge`,`first`,`last`,`city`,`stars`,`profileid`) VALUES (678912,'jane','smith','chicago',2,1);
INSERT INTO officers (`badge`,`first`,`last`,`city`,`stars`,`profileid`) VALUES (912345,'john','doe','denver',5,2);
INSERT INTO officers (`badge`,`first`,`last`,`city`,`stars`,`profileid`) VALUES (397389,'jane','doe','miami',1,3);

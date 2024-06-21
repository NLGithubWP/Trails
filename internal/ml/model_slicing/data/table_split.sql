CREATE TABLE census_int_train_left (
    id INT PRIMARY KEY,
    label INT,
    col1 INT, col2 INT, col3 INT, col4 INT, col5 INT,
    col6 INT, col7 INT, col8 INT, col9 INT, col10 INT,
    col11 INT, col12 INT, col13 INT, col14 INT, col15 INT,
    col16 INT, col17 INT, col18 INT, col19 INT, col20 INT
);

CREATE TABLE census_int_train_right (
    right_id SERIAL PRIMARY KEY,  -- Auto-generated primary key
    id INT REFERENCES census_int_train_left(id),  -- Foreign key reference to left table's ID
    col21 INT, col22 INT, col23 INT, col24 INT, col25 INT,
    col26 INT, col27 INT, col28 INT, col29 INT, col30 INT,
    col31 INT, col32 INT, col33 INT, col34 INT, col35 INT,
    col36 INT, col37 INT, col38 INT, col39 INT, col40 INT,
    col41 INT
);


INSERT INTO census_int_train_left (id, label, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20)
SELECT id, label, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20
FROM census_int_train;


INSERT INTO census_int_train_right (id, col21, col22, col23, col24, col25, col26, col27, col28, col29, col30, col31, col32, col33, col34, col35, col36, col37, col38, col39, col40, col41)
SELECT id, col21, col22, col23, col24, col25, col26, col27, col28, col29, col30, col31, col32, col33, col34, col35, col36, col37, col38, col39, col40, col41
FROM census_int_train;


SELECT
    l.id,
    l.label,
    l.col1, l.col2, l.col3, l.col4, l.col5, l.col6, l.col7, l.col8, l.col9, l.col10,
    l.col11, l.col12, l.col13, l.col14, l.col15, l.col16, l.col17, l.col18, l.col19, l.col20,
    r.col21, r.col22, r.col23, r.col24, r.col25, r.col26, r.col27, r.col28, r.col29, r.col30,
    r.col31, r.col32, r.col33, r.col34, r.col35, r.col36, r.col37, r.col38, r.col39, r.col40, r.col41
FROM
    census_int_train_left l
JOIN
    census_int_train_right r ON l.id = r.id limit 10;

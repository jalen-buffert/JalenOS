-- Priorities Table 

CREATE TABLE category(
    {
        category_id INT PRIMARY KEY,
        category VARCHAR(50)
    }
);

INSERT INTO category VALUES (1,'Career');
INSERT INTO category VALUES (2,'Investment');
INSERT INTO category VALUES (3,'Project');
INSERT INTO category VALUES (4,'Education');
INSERT INTO category VALUES (5,'Health');

CREATE TABLE importance(
    {
        importance_id INT PRIMARY KEY,
        importance VARCHAR(50) 
    }   
);

INSERT INTO importance VALUES (1,'High');
INSERT INTO importance VALUES (2,'Medium');
INSERT INTO importance VALUES (3,'Low');

CREATE TABLE status( 
    {
        status_id INT PRIMARY KEY,
        status VARCHAR(50)
    }
);

INSERT INTO status VALUES (1,'Not Started');
INSERT INTO status VALUES (2,'In Progress');
INSERT INTO status VALUES (3,'DND');    
INSERT INTO status VALUES (4,'Done');   

CREATE TABLE priorities(
    {
        priority_id INT PRIMARY KEY,
        title VARCHAR(50),
        action_needed VARCHAR(250),
        link VARCHAR,
        c_id INT references category(category_id),
        i_id INT references importance(importance_id),
        s_id INT references status(status_id),
    }
);
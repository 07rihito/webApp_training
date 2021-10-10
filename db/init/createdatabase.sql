CREATE DATABASE app;
USE app;

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255),
    passwd VARCHAR(255)
);

INSERT INTO users(id, username, email, passwd) VALUES(1, 'sample','sample@sample.com', 'sample');
INSERT INTO users(id, username, email, passwd) VALUES(2, 'test','test@test.com', 'test');
INSERT INTO users(id, username, email, passwd) VALUES(3, 'app','app@app.com', 'app');
INSERT INTO users(id, username, email, passwd) VALUES(4, 'user1', 'user1', 'user1');

-- add authority
GRANT ALL On app.* TO user1@"%";

-- CREATE TABLE foodlist(
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     eatdate DATE ,
--     foodname VARCHAR(255),
--     fee INT,
--     store VARCHAR(255)
-- );

-- ALTER TABLE foodlist ADD store VARCHAR(255);

-- INSERT INTO foodlist(date, name, fee, store) VALUES('2021-04-06', 'スパチキセット', 500, 'マクドナルド');
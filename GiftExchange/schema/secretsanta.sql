DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  userid serial NOT NULL,
  username text NOT NULL,
  PRIMARY KEY (userid)
);

INSERT INTO users (username) VALUES
('James'),
('Dennis'),
('Ming');
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  userid serial NOT NULL,
  username text NOT NULL,
  removed int DEFAULT 0,
  PRIMARY KEY (userid)
);

INSERT INTO users (username) VALUES
('James'),
('Dennis'),
('Ming');
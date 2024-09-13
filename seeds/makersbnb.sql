-- The job of this file is to reset the users, spaces, and bookings database tables.
-- This ensures that our tests and application are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) our tables
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them

-- Creating the 'users' table
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    username TEXT
);

-- Creating the 'spaces' table with a foreign key referencing 'users' (host)
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price_per_night INT,
    availability_start DATE,
    availability_end DATE,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
      REFERENCES users(id)
      ON DELETE CASCADE
);

-- Creating the 'bookings' table with foreign keys referencing 'users' and 'spaces'
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INT,
    user_id INT,
    booking_date DATE,
    CONSTRAINT fk_space FOREIGN KEY (space_id)
      REFERENCES spaces(id)
      ON DELETE CASCADE,
    CONSTRAINT fk_user_booking FOREIGN KEY (user_id)
      REFERENCES users(id)
      ON DELETE CASCADE
);

-- Finally, we add any records that are needed for the tests to run

-- Adding sample users
INSERT INTO users (email, password, username) VALUES ('guest1@example.com', 'password1', 'guest1');
INSERT INTO users (email, password, username) VALUES ('guest2@example.com', 'password2', 'guest2');
INSERT INTO users (email, password, username) VALUES ('host1@example.com', 'password3', 'host1');
INSERT INTO users (email, password, username) VALUES ('host2@example.com', 'password4', 'host2');

-- Adding sample spaces with hosts
INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) 
VALUES ('Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3);

INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) 
VALUES ('Tree House', 'A house my dad build in my backyard.', 125, '2024-10-11', '2024-11-30', 1);

INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) 
VALUES ('Mountain Cabin', 'A cozy cabin in the mountains.', 120, '2024-10-01', '2024-10-15', 4);

-- Adding sample bookings by guests
INSERT INTO bookings (space_id, user_id, booking_date) VALUES (1, 1, '2024-09-20');
INSERT INTO bookings (space_id, user_id, booking_date) VALUES (2, 2, '2024-10-10');
INSERT INTO bookings (space_id, user_id, booking_date) VALUES (3, 1, '2024-11-11');

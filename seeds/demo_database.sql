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

-- Adding sample users (24 in total)
INSERT INTO users (email, password, username) VALUES
('guest1@example.com', 'password1', 'guest1'),
('guest2@example.com', 'password2', 'guest2'),
('host1@example.com', 'password3', 'host1'),
('host2@example.com', 'password4', 'host2'),
('user5@example.com', 'password5', 'user5'),
('user6@example.com', 'password6', 'user6'),
('user7@example.com', 'password7', 'user7'),
('user8@example.com', 'password8', 'user8'),
('user9@example.com', 'password9', 'user9'),
('user10@example.com', 'password10', 'user10'),
('user11@example.com', 'password11', 'user11'),
('user12@example.com', 'password12', 'user12'),
('user13@example.com', 'password13', 'user13'),
('user14@example.com', 'password14', 'user14'),
('user15@example.com', 'password15', 'user15'),
('user16@example.com', 'password16', 'user16'),
('user17@example.com', 'password17', 'user17'),
('user18@example.com', 'password18', 'user18'),
('user19@example.com', 'password19', 'user19'),
('user20@example.com', 'password20', 'user20'),
('user21@example.com', 'password21', 'user21'),
('user22@example.com', 'password22', 'user22'), 
('user23@example.com', 'password23', 'user23'),
('user24@example.com', 'password24', 'user24');

-- Adding sample spaces (18 in total)
INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) VALUES
('Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3),
('Tree House', 'A house my dad build in my backyard.', 125, '2024-10-11', '2024-11-30', 1),
('Mountain Cabin', 'A cozy cabin in the mountains.', 120, '2024-10-01', '2024-10-15', 4),
('City Loft', 'Modern loft in the heart of downtown.', 200, '2024-09-20', '2024-12-31', 5),
('Lakeside Cottage', 'Peaceful cottage by the lake.', 140, '2024-10-05', '2024-11-15', 6),
('Desert Oasis', 'Unique stay in the middle of the desert.', 180, '2024-11-01', '2024-12-15', 7),
('Ski Chalet', 'Cozy chalet near popular ski slopes.', 250, '2024-12-01', '2025-03-31', 1),
('Countryside Barn', 'Converted barn in picturesque countryside.', 110, '2024-09-25', '2024-11-30', 9),
('Beachfront Bungalow', 'Small bungalow steps from the beach.', 160, '2024-10-10', '2024-12-20', 10),
('Urban Penthouse', 'Luxurious penthouse with city views.', 300, '2024-09-30', '2024-12-31', 11),
('Forest Retreat', 'Secluded cabin surrounded by forest.', 130, '2024-10-15', '2024-11-30', 12),
('Historic Townhouse', 'Charming townhouse in the old town.', 170, '2024-11-05', '2025-01-15', 13),
('Riverside Cabin', 'Rustic cabin on the river bank.', 140, '2024-10-20', '2024-12-10', 14),
('Island Bungalow', 'Tropical bungalow on a private island.', 280, '2024-12-15', '2025-04-30', 15),
('Mountain View Apartment', 'Apartment with stunning mountain views.', 190, '2024-11-10', '2025-02-28', 16),
('Seaside Villa', 'Spacious villa overlooking the sea.', 350, '2024-10-01', '2024-12-31', 17),
('Country Farmhouse', 'Traditional farmhouse in rural setting.', 160, '2024-09-20', '2024-11-30', 18),
('City Center Studio', 'Compact studio in prime city location.', 120, '2024-10-05', '2024-12-15', 1);


-- Adding sample bookings (23 in total)
INSERT INTO bookings (space_id, user_id, booking_date) VALUES
(1, 1, '2024-09-20'),
(2, 2, '2024-11-10'),
(3, 2, '2024-11-10'),
(4, 2, '2024-10-05'), 
(5, 4, '2024-10-20'),
(6, 5, '2024-11-10'),
(7, 6, '2024-12-15'),
(8, 7, '2024-10-01'),
(9, 8, '2024-11-05'),
(10, 9, '2024-10-15'),
(11, 10, '2024-11-20'),
(12, 11, '2024-12-01'),
(13, 12, '2024-10-25'),
(14, 13, '2025-01-15'),
(15, 14, '2024-12-20'), 
(16, 15, '2024-11-25'),
(17, 16, '2024-10-30'),
(18, 17, '2024-11-30'),
(3, 18, '2024-10-05'),
(18, 19, '2024-11-22'),
(17, 20, '2024-09-20'),
(1, 18, '2024-09-17'),
(1, 4, '2024-09-16');
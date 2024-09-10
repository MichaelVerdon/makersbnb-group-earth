# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
https://trello.com/b/PQZ5D50O/makers-bnb
```

```
Nouns:

users (guest, host), spaces, price per night, dates, description, avaibility, name of space, 
email, password, username


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| users                  | id, email, password, username
| spaces                 | id, name, description, price_per_night, availiable_dates, user_id_host
| bookings               | id, user_id_guest, space_id, date

1. Name of the first table (always plural): `users` 

    Column names: `id`, `email`, `password`, `username`

2. Name of the second table (always plural): `spaces` 

    Column names: `id`, `name`, `description`, `price_per_night`, 
                  `availability_start`, `availability_end` ,`user_id_host`

2. Name of the third table (always plural): `bookings` 

    Column names: `id`, `user_id_guest`, `space_id`, `date`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
email: text
password: text
username: text

Table: spaces
id: SERIAL
name: text
description: text
price_per_night: int
availability_start: date
availability_end: date
user_id: int

Table: bookings
id: SERIAL
space_id: int
user_id: int
booking_date: date
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
2. Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
            one to many              
 Users   ────────────────►   Spaces  

 o │                            │ o  
 n │                            │ n  
 e │                            │ e  
   │                            │    
 t │                            │ t  
 o │                            │ o  
   │                            │    
 m │                            │ m  
 a │                            │ a  
 n └────────►  Bookings  ◄──────┘ n  
 y                                y  

Table: foreign_key 

spaces: user
bookings: user, space
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
);

-- Then the table with the foreign key second.
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
-- The foreign key name is always {other_table_singular}_id
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 makersbnb_db < seeds/makersbnb.sql
```
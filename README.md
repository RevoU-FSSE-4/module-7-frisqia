[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZXimSQGf)

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    email VARCHAR(100) NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5)
    
);

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(191) NULL DEFAULT NULL
);
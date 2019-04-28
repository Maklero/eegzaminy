DROP TABLE IF EXISTS exam_model;
DROP TABLE IF EXISTS exams_list;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS temporary_users;
DROP TABLE IF EXISTS revoked_tokens;


CREATE TABLE exam_model (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    question TEXT COLLATE utf8_polish_ci NOT NULL,
    answer_a TEXT COLLATE utf8_polish_ci NOT NULL,
    answer_b TEXT COLLATE utf8_polish_ci NOT NULL,
    answer_c TEXT COLLATE utf8_polish_ci NOT NULL,
    answer_d TEXT COLLATE utf8_polish_ci NOT NULL,
    image_url TEXT COLLATE utf8_polish_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- there is fields like 'answer_a', but for this moment I still using only 'A' in current database

CREATE TABLE exams_list (
    id INT COLLATE utf8_polish_ci PRIMARY KEY AUTO_INCREMENT,
    exam_name TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) COLLATE utf8_polish_ci UNIQUE NOT NULL,
    password TEXT NOT NULL,
    last_login DATETIME,
    access_level INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

CREATE TABLE temporary_users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) COLLATE utf8_polish_ci UNIQUE NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

CREATE TABLE revoked_tokens (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    jti TEXT NOT NULL
);

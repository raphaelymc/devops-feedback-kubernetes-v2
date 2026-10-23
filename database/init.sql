
CREATE DATABASE IF NOT EXISTS devops_feedback;

USE devops_feedback;

CREATE TABLE IF NOT EXISTS comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    comentario VARCHAR(500) NOT NULL
);

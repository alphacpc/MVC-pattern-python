DROP DATABASE IF EXISTS ApiPythonDB;

CREATE DATABASE IF NOT EXISTS ApiPythonDB;

USE ApiPythonDB;

CREATE TABLE IF NOT EXISTS Address (
    idAddress int AUTO_INCREMENT,
    street varchar(100),
    suite varchar(50),
    city varchar(50),
    zipcode varchar(50),
    lat float,
    lng float,
    PRIMARY KEY (idAddress)
);

CREATE TABLE IF NOT EXISTS Company (
    idCompany int AUTO_INCREMENT,
    name_Company varchar(100),
    catchPhrase varchar(100),
    bs varchar(100),
    PRIMARY KEY (idCompany)
);

CREATE TABLE IF NOT EXISTS Users (
    idUser int AUTO_INCREMENT,
    name_User varchar(50),
    username varchar(50),
    email varchar(100),
    idAddress_User int,
    phone varchar(50),
    website varchar(100),
    idCompany_User int,
    CONSTRAINT PK_User PRIMARY KEY (idUser),
    FOREIGN KEY (idAddress_User) REFERENCES Address(idAddress),
    FOREIGN KEY (idCompany_User) REFERENCES Company(idCompany)
);


CREATE TABLE IF NOT EXISTS Posts (
    idPost int AUTO_INCREMENT,
    title_Post varchar(150),
    body text,
    userId_Post int,
    PRIMARY KEY (idPost),
    FOREIGN KEY (userId_Post) REFERENCES Users(idUser)
);


CREATE TABLE IF NOT EXISTS Comments (
    idComment int AUTO_INCREMENT,
    name_Comment varchar(150),
    email varchar(100),
    body text,
    postId int,
    PRIMARY KEY (idComment),
    FOREIGN KEY (postId) REFERENCES Posts(idPost)
);

CREATE TABLE IF NOT EXISTS Albums (
    idAlbum int AUTO_INCREMENT,
    title_Album varchar(150),
    userId_Album int,
    PRIMARY KEY (idAlbum),
    FOREIGN KEY (userId_Album) REFERENCES Users(idUser)
);

CREATE TABLE IF NOT EXISTS Photos (
    idPhoto int AUTO_INCREMENT,
    title_Photo varchar(150),
    url_Photo varchar(150),
    thumbnailUrl varchar(150),
    albumId int,
    PRIMARY KEY (idPhoto),
    FOREIGN KEY (albumId) REFERENCES Albums(idAlbum)
);

CREATE TABLE IF NOT EXISTS Todos (
    idTodo int AUTO_INCREMENT,
    title_Todo varchar(150),
    userId_Todo int,
    PRIMARY KEY (idTodo),
    FOREIGN KEY (userId_Todo) REFERENCES Users(idUser)
);
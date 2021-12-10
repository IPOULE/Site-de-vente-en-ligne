DROP TABLE IF EXISTS Livre;

CREATE TABLE Livre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre  TEXT NOT NULL,
    date_parution   DATE,
    prix TEXT,
    lien_image TEXT
);

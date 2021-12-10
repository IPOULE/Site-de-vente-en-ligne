import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

from website import create_app

app=create_app()

if __name__ == '__main__':
    app.run(debug=True)

app=Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('website/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_livre(id_livre):
    conn=get_db_connection()
    livre = conn.execute('SELECT * FROM Livre WHERE id =?',
                            (id_livre,)).fetchone()
    conn.close()
    if livre is None:
        abort(404)
    return livre

@app.route("/")
def index():
    conn = get_db_connection()
    livres = conn.execute('SELECT * FROM Livre').fetchall()
    conn.close()
    return render_template("index.html", livres=livres)

@app.route('/<int:id_livre>')
def livre(id_livre):
    book = get_livre(id_livre)
    return render_template('test.html', book=book)

if __name__ == "__main__":
    app.run(debug=True)
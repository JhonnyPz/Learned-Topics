"""import sqlite3"""
import sqlite3 as sql
import os

def createsqlite():
    """Createsqlite"""
    filename = r"./Sqlite3/game.db"
    if os.path.exists(filename):
        os.remove(filename)
        createdb()
    else:
        createdb()

def createdb():
    """create database"""
    conn = sql.connect("./Sqlite3/game.db")
    conn.commit()
    conn.close()
    print("database created...")


def createtable():
    """create tableble"""
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS players (
          nickname text,
          level integer,
          edad integer
      )"""
    )
    conn.commit()
    conn.close()
    print("table created...")


def insertrow(nickname, level, edad):
    """insert a row into the database"""
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO players VALUES ('{nickname}', '{level}', '{edad}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    print("inserted player: " + nickname)


def insertrows(playerslist):
    """insert multiple rows into the database"""
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    instruction = "INSERT INTO players VALUES (?, ?, ?)"
    cursor.executemany(instruction, playerslist)
    print("inserted row: " + str(len(playerslist)))
    conn.commit()
    conn.close()


def readrows():
    """read a rows from the database"""
    print("read rows from the database")
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

    table(datos)

def readorder(field):
    """Read the order field from the database"""
    print(f"raed rows from the database Order by {field}")
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    introduction = f"SELECT * FROM players ORDER BY {field} DESC"
    cursor.execute(introduction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

    table(datos)

def search(nickname):
    """Search for a nickname"""
    print("search player: " + nickname)
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    introduction = "SELECT * FROM players WHERE nickname = '{nickname}'".format
    cursor.execute(introduction(nickname=nickname))
    datos = cursor.fetchone()
    conn.commit()
    conn.close()

    print(datos)

def update_nick(nickname, new_nickname):
    """Update a nickname"""
    conn = sql.connect("./Sqlite3/game.db")
    cursor = conn.cursor()
    introduction = f"UPDATE players SET nickname = '{new_nickname}' WHERE nickname = '{nickname}'"
    cursor.execute(introduction)
    conn.commit()
    conn.close()
    print("Success Update players name: ")
    search(new_nickname)

def delete_players(check):
    """Delete a list of players"""
    if check is not False or check is not None:
        conn = sql.connect("./Sqlite3/game.db")
        cursor = conn.cursor()
        introduction = "DELETE FROM players WHERE level <= 50"
        cursor.execute(introduction)
        conn.commit()
        conn.close()
        print("Success Delete playerslist players with level <= 50")
        readrows()

def table(datos):
    """print table players"""
    row = "|{name1:^8}|{name2:^5}|{name3:^4}|".format
    for tup in datos:
        print(row(name1=tup[0], name2=tup[1], name3=tup[2]))

if __name__ == '__main__':
    createsqlite()
    createtable()

    insertrow("Art", 100, 20)
    playerlist = [
        ("Ray", 20, 35),
        ("John", 50, 46),
        ("Oscar", 80, 32)
        ]
    insertrows(playerlist)

    readrows()
    readorder("level")

    update_nick("Art","Arthur")
    delete_players(True)

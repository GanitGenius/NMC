import sqlite3

conn = sqlite3.connect("nmc.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE users(
        id text,
        passwd text,
        mob text
    )"""
)

c.execute(
    """CREATE TABLE users_schedule(
        id text,
        hr integer,
        mn integer
    )"""
)


def insert_user(user):
    with conn:
        c.execute(
            "INSERT INTO users VALUES (:id, :passwd)",
            {"id": user.id, "passwd": user.passwd, "mob": user.mob},
        )


def get_user_by_id(id):
    c.execute("SELECT * FROM users WHERE id=:id", {"id": id})
    return c.fetchone()


def get_user_schedule_by_id(id):
    c.execute("SELECT * FROM users_schedule WHERE id=:id", {"id": id})
    return c.fetchall()


def add_user_schedule_by_id(id, hr, mn):
    with conn:
        c.execute(
            "INSERT INTO users_schedule VALUES (:id, :hr, :mn)",
            {"id": id, "hr": hr, "mn": mn},
        )


def remove_user_schedule_by_id(id, hr, mn):
    with conn:
        c.execute(
            "DELETE FROM users WHERE id=:id AND hr=:hr AND mn=:mn",
            {"id": id, "hr": hr, "mn": mn},
        )


conn.close()

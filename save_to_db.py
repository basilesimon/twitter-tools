import MySQLdb


db = MySQLdb.connect(host="",
                     user="",
                     passwd="",
                     db="",
                     charset="utf8")


def save_to_db(author, text, url, id_str):
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Tweets(Id INT PRIMARY KEY AUTO_INCREMENT, \
                Author VARCHAR(255), \
                Text VARCHAR(255), \
                Url VARCHAR(255), \
                Tweet_Id VARCHAR(255), \
                Screenshot INT, \
                Deleted INT)")

    try:
        cur.execute("""INSERT INTO Tweets(Author, Text, Url, Tweet_Id, Screenshot, Deleted)
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (author, text, url, id_str, 0, 0))
        db.commit()
        print "Wrote to database:", author, id_str
    except MySQLdb.Error, e:
        print "Error", e.args[0], e.args[1]
        db.rollback()
        print "ERROR writing database"

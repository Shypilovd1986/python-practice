import mysql.connector as mysql


def main():
    con = mysql.connect(host='localhost', user='root', password='19865421', database='library')
    cur = con.cursor()

    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    print(f'MySQL version {version}')

    cur.execute('SELECT * FROM books')
    # we use object cur as iterator
    # or we can use fetchall()
    # rows = cur.fetchall()
    # for book in rows:
    #     print(book)

    for book in cur:
        print(book)

    # mysql.connector.connect().cursor().execute()

    cur.close()
    con.close()


if __name__ == '__main__':
    main()

import sqlite3


def main():
    con = sqlite3.connect("mydb")
    cur = con.cursor()

    cur.execute("SELECT sqlite_version()")
    version = cur.fetchone()[0]
    print(f'SQLite version {version}')

    cur.close()
    con.close()


if __name__ == '__main__':
    main()

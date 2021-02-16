import sqlite3 as sql
# usersValue = str(input("> "))
con = sql.connect('test.db')
with con:
    cur = con.cursor()
    for i in range(1000):
        usersValue = str(input("> "))
        cur.execute(f"SELECT field8 from '_cities' WHERE field8 = '{usersValue}';")
        rows = cur.fetchone()

        try:
            if usersValue.lower() == rows[0].lower():
                print("Nice! next step:")
        except TypeError:
            print("Idiot")
            exit(0)
        nextValue = usersValue[-1].upper()
        cur.execute(f"SELECT field8 from '_cities' WHERE field8 LIKE '{nextValue}%';")
        rows = cur.fetchone()
        print(rows[0])
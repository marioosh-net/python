import MySQLdb

conn = MySQLdb.connect("localhost", "test", "", "test");
c = conn.cursor();

# select
c.execute("SELECT * FROM texts");
rows = c.fetchall()
for r in rows:
    print r

# insert
c.execute("INSERT INTO texts (textkey, en,de) VALUES('key', 'english', 'deutch')")
conn.commit()


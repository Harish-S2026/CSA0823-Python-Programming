import sqlite3,csv,io
def inspect(text,delimiter=","):
    if not text.strip():return "Rejected: empty file"
    r=csv.DictReader(io.StringIO(text),delimiter=delimiter)
    if not r.fieldnames or not {"station","date","pm25"}.issubset(r.fieldnames):
        return "Rejected: missing column or wrong delimiter"
    return "Accepted rows: "+str(sum(1 for _ in r))
def main():
    con=sqlite3.connect(":memory:");con.execute("CREATE TABLE aq(station,day,pm25)")
    rows=[("Adyar","2026-10-01",48.),("Guindy","2026-10-01",95.),("Guindy","2026-10-03",121.),("Adyar","2026-10-04",60.)]
    con.executemany("INSERT INTO aq VALUES(?,?,?)",rows);con.commit()
    def avg(name):return con.execute("SELECT AVG(pm25) FROM aq WHERE station=?",(name,)).fetchone()[0]
    print(avg("Adyar"),avg("Guindy"));print(avg("Adyar' OR '1'='1"))
    print(inspect("station,date\\nAdyar,2026-10-01"))
    print(inspect("station;date;pm25\\nAdyar;2026-10-01;48"))
    print(inspect(""))
    print("Unsafe query illustration only: SELECT ... WHERE station = 'Adyar' OR '1'='1'")
    con.close()
if __name__=="__main__":main()

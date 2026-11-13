import csv,io,sqlite3
RAW="""station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""
def load_clean(text):
    rows=[]
    for r in csv.DictReader(io.StringIO(text)):
        v=r["pm25"].strip()
        if v.upper() in ("","NA","N/A"):continue
        try:x=float(v)
        except ValueError:continue
        if 0<=x<=999:rows.append((r["station"].strip().title(),r["date"],x))
    return rows
def min_max(v):
    if not v:return []
    lo,hi=min(v),max(v)
    return [0.0 if hi==lo else round((x-lo)/(hi-lo),3) for x in v]
def main():
    rows=load_clean(RAW);print(rows);print(min_max([r[2] for r in rows]))
    con=sqlite3.connect(":memory:");con.execute("CREATE TABLE aq(station,day,pm25)")
    con.executemany("INSERT INTO aq VALUES(?,?,?)",rows);con.commit()
    for sql in ["SELECT station,AVG(pm25) FROM aq GROUP BY station",
                "SELECT station,day,AVG(pm25) FROM aq GROUP BY station,day",
                "SELECT station,day,AVG(pm25) m FROM aq GROUP BY station,day ORDER BY m DESC LIMIT 1"]:
        print(list(con.execute(sql)))
    con.close()
if __name__=="__main__":main()

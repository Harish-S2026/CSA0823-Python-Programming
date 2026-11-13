import sqlite3,time
from task09_helpers import COMPLAINTS,label,summarise
def main():
    # Demonstration baseline only; replace with independent manual labels for assessment.
    baseline=["negative" if any(w in c.lower() for w in ("smoke","dirty","bad","broken","rude","slow"))
              else "positive" if any(w in c.lower() for w in ("clean","good","helpful","improved","fast"))
              else "neutral" for c in COMPLAINTS]
    predicted=[label(c) for c in COMPLAINTS]
    agree=sum(a==b for a,b in zip(baseline,predicted))
    print(f"Agreement with rule baseline: {agree}/50 ({agree*2}%). Not independent human validation.")
    print("Summary:",summarise(" ".join(COMPLAINTS[:10])))
    c=sqlite3.connect(":memory:");c.execute("CREATE TABLE aq(station,day,pm25)")
    c.executemany("INSERT INTO aq VALUES(?,?,?)",[("Adyar","2026-10-01",48),("Adyar","2026-10-01",52),("Guindy","2026-10-01",95)])
    q="SELECT AVG(pm25) FROM aq WHERE station=? AND day=?"
    t=time.perf_counter()
    for _ in range(1000):c.execute(q,("Adyar","2026-10-01")).fetchone()
    before=time.perf_counter()-t;c.execute("CREATE INDEX idx_station_day ON aq(station,day)")
    t=time.perf_counter()
    for _ in range(1000):c.execute(q,("Adyar","2026-10-01")).fetchone()
    after=time.perf_counter()-t
    print(f"1000 lookups before index={before:.6f}s after={after:.6f}s")
    print("Tiny in-memory data may not show an index benefit; repeat on realistic data.")
    c.close()
if __name__=="__main__":main()

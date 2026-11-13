from collections import defaultdict
from datetime import date,timedelta
from statistics import mean
import sqlite3,time,cProfile,pstats
def generate(n):
    rows=[];start=date(2026,1,1)
    for s in range(n):
        for d in range(365):
            day=(start+timedelta(days=d)).isoformat()
            for h in range(24):rows.append((f"S{s+1:03}",day,h,float(20+s%15+d%30+h%12)))
    return rows
def loops(rows):
    g=defaultdict(list)
    for s,d,h,v in rows:g[s,d].append(v)
    return {k:mean(v) for k,v in g.items()}
def sql(rows):
    c=sqlite3.connect(":memory:");c.execute("CREATE TABLE r(s,d,h,v)")
    c.executemany("INSERT INTO r VALUES(?,?,?,?)",rows)
    out=dict(((s,d),v) for s,d,v in c.execute("SELECT s,d,AVG(v) FROM r GROUP BY s,d"));c.close();return out
def pandas_method(rows):
    import pandas as pd
    return pd.DataFrame(rows,columns=["s","d","h","v"]).groupby(["s","d"])["v"].mean().to_dict()
if __name__=="__main__":
    for n in (1,12,120):
        r=generate(n);t=time.perf_counter();a=loops(r);tl=time.perf_counter()-t
        t=time.perf_counter();b=sql(r);ts=time.perf_counter()-t
        assert a==b
        print(f"{n} stations / {len(r)} rows: loops={tl:.4f}s SQL incl. load={ts:.4f}s")
        try:
            t=time.perf_counter();p=pandas_method(r);print("pandas=",round(time.perf_counter()-t,4),"s; groups=",len(p))
        except ImportError:print("Install pandas to run pandas comparison.")
    prof=cProfile.Profile();prof.enable();loops(generate(12));prof.disable();pstats.Stats(prof).sort_stats("cumtime").print_stats(8)

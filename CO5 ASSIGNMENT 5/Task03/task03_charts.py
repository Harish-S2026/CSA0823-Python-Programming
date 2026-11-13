from collections import defaultdict
from statistics import mean
DATA=[("Adyar","2026-10-01",1,48,28),("Adyar","2026-10-01",2,52,29),
("Adyar","2026-10-02",1,61,30),("Guindy","2026-10-01",1,95,31),
("Guindy","2026-10-01",2,90,30),("Guindy","2026-10-02",1,121,32)]
def summary(rows):
    g=defaultdict(list)
    for s,d,h,p,t in rows:g[s,d].append(p)
    return [(s,d,min(v),max(v),mean(v),len(v)) for (s,d),v in sorted(g.items())]
def charts(rows):
    import matplotlib.pyplot as plt
    daily=defaultdict(list); station=defaultdict(list); hour=defaultdict(list)
    for s,d,h,p,t in rows:daily[d].append(p);station[s].append(p);hour[h].append(p)
    plt.figure(); ds=sorted(daily);plt.plot(ds,[mean(daily[d]) for d in ds],marker="o")
    plt.title("Daily PM2.5 Trend");plt.xlabel("Date");plt.ylabel("PM2.5");plt.xticks(rotation=30);plt.tight_layout();plt.savefig("trend.png");plt.close()
    plt.figure(); names=sorted(station);plt.bar(names,[mean(station[n]) for n in names])
    plt.title("Station Comparison");plt.xlabel("Station");plt.ylabel("Mean PM2.5");plt.savefig("stations.png");plt.close()
    plt.figure();plt.scatter([r[4] for r in rows],[r[3] for r in rows])
    plt.title("Temperature vs PM2.5");plt.xlabel("Temperature C");plt.ylabel("PM2.5");plt.savefig("scatter.png");plt.close()
    plt.figure(); hs=sorted(hour);plt.bar([str(h) for h in hs],[mean(hour[h]) for h in hs])
    plt.title("Mean PM2.5 by Hour");plt.xlabel("Hour");plt.ylabel("Mean PM2.5");plt.savefig("hours.png");plt.close()
if __name__=="__main__":
    print("Daily summary:",summary(DATA))
    try: charts(DATA);print("Charts saved.")
    except ImportError: print("Install matplotlib: pip install matplotlib")

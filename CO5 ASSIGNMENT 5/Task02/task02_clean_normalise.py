import statistics
def clean(rows):
    result=[]; seen=set()
    for r in rows:
        key=(r["station"].strip().title(),r["date"],int(r["hour"]))
        if key in seen: continue
        seen.add(key); x=dict(r); x["station"]=key[0]
        for col in ("pm25","pm10","no","temperature"):
            try: x[col]=float(r[col]) if r[col].strip().upper() not in ("","NA","N/A") else None
            except (ValueError,AttributeError): x[col]=None
        for col in ("pm25","pm10","no"):
            if x[col] is not None and (x[col]<0 or x[col]>999): x[col]=None
        if x["temperature"] is not None and r.get("unit","C").upper()=="F":
            x["temperature"]=(x["temperature"]-32)*5/9
        result.append(x)
    for station in {x["station"] for x in result}:
        vals=[x["pm25"] for x in result if x["station"]==station and x["pm25"] is not None]
        if vals:
            med=statistics.median(vals)
            for x in result:
                if x["station"]==station and x["pm25"] is None: x["pm25"]=med
    return result
def minmax(v):
    if not v:return []
    lo,hi=min(v),max(v)
    return [0.0 if hi==lo else round((x-lo)/(hi-lo),3) for x in v]
def zscore(v):
    if not v:return []
    m=statistics.mean(v); sd=statistics.pstdev(v)
    return [0.0 if sd==0 else round((x-m)/sd,3) for x in v]
if __name__=="__main__":
    data=[{"station":"adyar","date":"2026-10-01","hour":"1","pm25":"48","pm10":"80","no":"2","temperature":"86","unit":"F"},
          {"station":"adyar","date":"2026-10-01","hour":"2","pm25":"NA","pm10":"90","no":"3","temperature":"30","unit":"C"}]
    out=clean(data); print(out); print(minmax([x["pm25"] for x in out]))

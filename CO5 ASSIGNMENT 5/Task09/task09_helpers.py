import re
from collections import Counter
POS={"good","clean","fast","helpful","improved"};NEG={"bad","dirty","slow","rude","smoke","broken"};NEGATORS={"not","never","no"}
def label(text):
    w=re.findall(r"[a-z']+",text.lower());score=0
    for i,x in enumerate(w):
        v=1 if x in POS else -1 if x in NEG else 0
        if i and w[i-1] in NEGATORS:v=-v
        score+=v
    return "positive" if score>0 else "negative" if score<0 else "neutral"
def summarise(text,k=3):
    sentences=re.split(r"(?<=[.!?])\\s+",text.strip());stop={"the","a","an","is","are","and","of","to","in","it"}
    freq=Counter(x for x in re.findall(r"[a-z']+",text.lower()) if x not in stop)
    return " ".join(x[2] for x in sorted([(sum(freq[w] for w in re.findall(r"[a-z']+",s.lower()) if w not in stop),-i,s) for i,s in enumerate(sentences)],reverse=True)[:k])
COMPLAINTS=[
"Smoke is coming from the factory near the school.","The road near the market is dirty and dusty.","The bus service is fast and helpful today.","Air quality is bad near the main road.","Street cleaning has improved this week.",
"The monitoring station display is broken.","Traffic is slow and smoke is heavy in the evening.","The staff were not helpful when I called.","The park area is clean and pleasant.","There is no update about the pollution complaint.",
"Smoke levels seem high near the bus stand.","The roads are clean after the morning sweep.","The response team was helpful and fast.","Construction dust makes the air dirty.","The air is not good near the junction.",
"The complaint portal is slow today.","Factory smoke was noticed near the river.","The street is clean but traffic is noisy.","The service was not bad this time.","Air quality improved after rain.",
"Garbage burning causes smoke near homes.","The bus was fast but the stop was dirty.","The sensor is broken and shows no reading.","The response was rude and unhelpful.","The new cleaning work is good.",
"Smoke and dust are affecting the school area.","The road is not clean near the station.","The helpline was helpful.","Pollution is bad during peak traffic.","The monitoring app is fast and clear.",
"The area smells of smoke every night.","The road cleaning has not improved.","The air is clean near the beach.","Officials gave no useful update.","Traffic is slow near the bridge.",
"The complaint was handled well.","The factory released smoke this morning.","The local street is dirty after the event.","Air quality is good today.","The sensor reading looks unusual.",
"The team was not rude and responded quickly.","Smoke is not reduced near the industrial area.","The bus service improved recently.","The public display is broken again.","The roadside is clean but air is bad.",
"The officer was helpful and polite.","Heavy traffic creates smoke and dust.","The monitoring station is working well.","The complaint system is not fast.","Air pollution remains a serious concern."]

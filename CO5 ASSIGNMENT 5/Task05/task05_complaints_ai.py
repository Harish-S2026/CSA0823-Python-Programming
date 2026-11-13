import re
from collections import Counter
POS={"good","clean","fast","helpful","improved"};NEG={"bad","dirty","slow","rude","smoke","broken"};NEGATORS={"not","never","no"}
def score(text):
    words=re.findall(r"[a-z']+",text.lower());total=0
    for i,w in enumerate(words):
        v=1 if w in POS else -1 if w in NEG else 0
        if i and words[i-1] in NEGATORS:v=-v
        total+=v
    return total
def label(text):
    n=score(text);return "positive" if n>0 else "negative" if n<0 else "neutral"
def summarise(text,k=2):
    sentences=re.split(r"(?<=[.!?])\\s+",text.strip()); stop={"the","a","an","is","are","and","of","to","in","it"}
    freq=Counter(w for w in re.findall(r"[a-z']+",text.lower()) if w not in stop)
    ranked=[]
    for i,s in enumerate(sentences):
        ranked.append((sum(freq[w] for w in re.findall(r"[a-z']+",s.lower()) if w not in stop),-i,s))
    return " ".join(x[2] for x in sorted(ranked,reverse=True)[:k])
if __name__=="__main__":
    for c in ["Roads are clean and the bus was fast.","Smoke from factory, air is bad.","The staff were not helpful.","Not bad, service improved."]:
        print(f"{label(c):8} | {c}")
    print(summarise("Road is dirty. Smoke is near school. Bus service is slow."))

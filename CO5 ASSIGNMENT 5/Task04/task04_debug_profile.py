import logging,time,cProfile,pstats
from io import StringIO
logging.basicConfig(level=logging.INFO)
def clean(values):
    result=[]
    for x in values:
        assert isinstance(x,(int,float))
        if x>=0:result.append(x)
    logging.info("Kept %d readings",len(result))
    return result
if __name__=="__main__":
    values=[10,20,-1,30]*10000
    t=time.perf_counter(); out=clean(values); print("Elapsed:",time.perf_counter()-t,"Valid:",len(out))
    p=cProfile.Profile();p.enable();clean(values);p.disable()
    s=StringIO();pstats.Stats(p,stream=s).sort_stats("cumulative").print_stats(5);print(s.getvalue())

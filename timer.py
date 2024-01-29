import time
def timer(anything):
    start = time.time()
    anything
    print("Time execution: %s seconds" % (time.time()-start))

timer(2*10000000)
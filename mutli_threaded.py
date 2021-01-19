import time
from threading import Thread

def io_task():
    time.sleep(2.5)

t1 = Thread(target=io_task)
t2 = Thread(target=io_task)

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
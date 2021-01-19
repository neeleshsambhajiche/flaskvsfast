import time

def io_task():
    time.sleep(5)

start = time.time()
io_task()
end = time.time()

print('Time taken in seconds -', end - start)
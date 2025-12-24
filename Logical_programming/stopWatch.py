import time

input("Press enter to start the timer")
start = time.time()

input("Press enter to stop the watch")

stop = time.time()

elapsed_time = stop - start

print("TOtal time: ", elapsed_time)

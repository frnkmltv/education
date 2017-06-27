import threading
import time

import philosophers

spoons = [threading.Lock() for n in range(1, 9)]
persons = [
    philosophers.Philosopher(name=str(counter + 1), max_time_for_eat=13, right_fork=spoons[counter - 1],
                             left_fork=spoons[counter]) for counter in range(8)]
print(spoons, persons)
philosophers.Philosopher.running = True
for p in persons:
    p.start()
time.sleep(100)
philosophers.Philosopher.running = False

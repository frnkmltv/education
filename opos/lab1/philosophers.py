# -*- coding: utf-8 -*-
import random
import threading
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, name, max_time_for_eat, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name, self.max_time_for_eat, self.left_fork, self.right_fork = name, max_time_for_eat, left_fork, right_fork

    def eat(self):
        while self.running:
            self.left_fork.acquire(True)
            if self.right_fork.acquire(False):
                self.eating()
                self.left_fork.release()
                self.right_fork.release()
            else:
                self.left_fork.release()
                print(u'Философ %s ожидает свободных вилок.' % self.name)
                return

    def eating(self):
        print(u'Философ %s ест спагетти.' % self.name)
        time.sleep(random.randint(3, self.max_time_for_eat))

    def run(self):
        while self.running:
            # time.sleep(random.randint(3, self.max_time_for_eat))
            self.eat()
            time.sleep(random.randint(5, self.max_time_for_eat + 3))
            print(u'Философ %s беседует.' % self.name)

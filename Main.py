import os
from modules.TodoList import TodoList
from modules.TodoListChecker import checker
import threading
import time

# This is a sample intended application of the to-do cli

if __name__ == "__main__":
    # if any previous file (in ./.data) exist, extract data from there, else make an empty list
    t = TodoList.load_lst() if os.path.exists('./.data') else TodoList()
    # This will be done via interactive CLI (WIP)
    try:
        # add some to-dos
        t.add_todo(
            task='Wash Dishes',
            description="Don't forget to use Vim bar also",
            minute_deadline_offset=1.5)

        t.add_todo(
            task='Hang Clothes',
            description="Also install new hanging rope",
            minute_deadline_offset=0.5)

        t.add_todo(
            task='Run Washing Machine',
            description="Also use Comfort in the end",
            minute_deadline_offset=1)

        # multithreading used here such that it doesn't interfere with Future to-do Insertion
        t1 = threading.Thread(target=checker, args=(t,), name='t1')
        # this makes the thread auto close when the parent thread closes
        t1.setDaemon(True)
        t1.start()

        # WIP: as there should be a Interactive CLI, there will be something
        # similar to an infinite loop with KeyboardInterrupt/exit() close
        # here this is simulated as a sleep timer
        time.sleep(100)
    except KeyboardInterrupt:
        # If we get an KeyboardInterrupt, save the To-do list in a file
        t.store_lst()

from .Todo import Todo
import datetime
import os
import pickle
import heapq


class TodoList:
    """
    - The To-do List Object which stores the To-do in a Priority Queue (Heap).
    - Heap is based on lowest datetime first to get easy access to most current
    incoming To-do
    """

    def __init__(self) -> None:
        self.data = []

    def add_todo(self, task: str, description: str, minute_deadline_offset: float = 1) -> None:
        """
        adds a to-do in the todo_list
        Args:
            task: heading of To-do
            description: description of the To-do
            minute_deadline_offset: after how many min do you need to-do notify?

        Returns:

        """
        heapq.heappush(
            self.data,
            Todo(task,
                 description,
                 datetime.datetime.now() + datetime.timedelta(minutes=minute_deadline_offset)
                 )
        )

    def add_todo_dtm(self, task: str, description: str, dtm: datetime):
        heapq.heappush(self.data, Todo(task, description, dtm))

    def curr_todo_done(self):
        """
        Call this when the most current event is done, this will delete
        that to-do from the list
        """
        heapq.heappop(self.data)

    def get_next_todo(self):
        """
        Return the next upcoming To-do in the to-do list

        Returns: To-do Object
        """
        try:
            return self.data[0]
        except IndexError:
            print('Todo List is empty, consider adding some Todo')

    def list_size(self):
        """Returns the size of the to-do list"""
        return len(self.data)

    def store_lst(self):
        """stores list data in a file"""
        if self.list_size() > 0:
            store_file = open('./.data', 'wb')
            pickle.dump(self.data, store_file)
            store_file.close()

    @staticmethod
    def load_lst():
        """loads list from datafile and returns the list"""
        load_file = open('./.data', 'rb')
        lst = pickle.load(load_file)
        load_file.close()
        os.remove('./.data')

        # lst now contains a list of strings made by __repr__ of To-do
        # the string representation of To-do had task, description and date time in csv format
        # converting them the list of list of strings
        lst = [str(i).split(',') for i in lst]

        # now for each i in lst -> i[0] = task; i[1] = desc, i[2] = datetime in string format
        t = TodoList()
        for i in lst:
            t.add_todo_dtm(
                i[0],
                i[1],
                datetime.datetime.strptime(i[2], '%Y-%m-%d %H:%M:%S.%f'))

        return t

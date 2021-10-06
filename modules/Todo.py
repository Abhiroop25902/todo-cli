import datetime


class Todo:
    """
    A single to-do with a task and a deadline
    """
    def __init__(self, task: str, desc: str, dtm: datetime):
        """
        Constructor for the to-do object
        Args:
            task: The To-do Heading
            desc: To-do Description
            dtm: datetime object
        """
        self.task = task
        self.desc = desc
        self.dtm = dtm

    def get_task(self):
        """Return the task of the to-do"""
        return self.task

    def get_deadline(self) -> datetime:
        """returns the deadline"""
        return self.dtm

    def get_desc(self) -> str:
        """return the To-do Description"""
        return self.desc

    def __lt__(self, other) -> bool:
        """less than operator override"""
        return self.get_deadline() < other.get_deadline()

    def __repr__(self) -> str:
        """representation override"""
        return f"{self.get_task()},{self.get_desc()},{self.get_deadline()}"

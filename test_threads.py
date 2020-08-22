from dao import darts_match_dao_thread_safe_singleton
from domain import darts_match

import threading


class AddThread(threading.Thread):
    def __init__(self, thread_id, name, match):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.match = match
        self.dao = darts_match_dao_thread_safe_singleton.DartsMatchDao.get_instance()

    def run(self):
        print("Starting " + self.name)
        self.dao.add(self.match)
        print("Exiting " + self.name)


dart_match1 = darts_match.DartsMatch('501', 'Dupe', 'Dup2')
thread1 = AddThread(1, "Thread-1", dart_match1)

dart_match2 = darts_match.DartsMatch('501', 'Dupe', 'Dup2')
thread2 = AddThread(2, "Thread-2", dart_match2)

thread1.start()
thread2.start()

print("Exiting main thread.")

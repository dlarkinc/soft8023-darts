from tinydb import TinyDB, Query

import threading
import time

class DartsMatchDao:

    def __init__(self):
        self.db = TinyDB('db.json')
        self.lock = threading.Lock()

    def add(self, match):
        self.lock.acquire()

        time.sleep(4)

        Match = Query()
        if not self.db.contains(Match.player1 == match.player1):
           self.db.insert({'type': match.type, 'player1': match.player1, 'player2': match.player2})

        print('Insert attempted on ' + match.player1)

        self.lock.release()
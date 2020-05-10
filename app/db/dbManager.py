
import mongoengine as mongo


class DBInterface(object):
    def __init__(self, **config):
        self.config = config.get('config')
        self.conn = self._connect()

    def _connect(self):
        return mongo.connect(**self.config)

    def connection(self):
        return self.conn

    def cursor(self):
        return self.conn.cursor()

    def transaction(self):
        self.conn.start_transaction()

    def commit(self):
        self.conn.commit()

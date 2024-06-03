import pymysql

class Connector :
    conn = None
    host = '127.0.0.1'
    user = 'root'
    password = '1234'
    db = 'project_1_db'
    charset = 'utf8'

    def get_connection(self) :
        if self.conn is None :
            self.conn = pymysql.connect(host = self.host, 
                                        user = self.user, 
                                        password = self.password, 
                                        db = self.db, 
                                        charset = self.charset)
        return self.conn
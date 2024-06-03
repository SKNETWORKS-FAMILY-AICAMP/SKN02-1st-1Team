import pymysql

class Connector :
    __connector = None
    host = '127.0.0.1'
    user = 'root'
    password = '1234'
    db = 'project_1_db'
    charset = 'utf8'

    def __init__(self) :
        if self.__connector is None :
            self.__connector = pymysql.connect(host = self.host, 
                                        user = self.user, 
                                        password = self.password, 
                                        db = self.db, 
                                        charset = self.charset)
        else :
            raise Exception("You already have a connector!")

    @classmethod
    def get_connection(cls) :
        if not cls.__connector :
            cls.__connector = pymysql.connect(host = cls.host, 
                                        user = cls.user, 
                                        password = cls.password, 
                                        db = cls.db, 
                                        charset = cls.charset)
        return cls.__connector
    
    @classmethod
    def select_all(cls, table_name) :
        cursor = cls.get_connection().cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        return cursor
import MySQLdb



class PyScripTalk():
    DatabaseAdress = "localhost"
    Username = "root"
    Password = ""
    DatabaseName = "pyscriptalk"
    TabName = "messages"

    def init(self):
        
        self.db = MySQLdb.connect(self.DatabaseAdress, self.Username, self.Password, \
                             self.DatabaseName)

        

    def test(self):
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM %s " % self.TabName)
        return self.cursor.fetchall()

    def addMessage(self, messagetext, auth):
        try:
            self.cursor.execute("INSERT INTO %s (content, auth) VALUES ('%s', '%s') " % (self.TabName, messagetext, auth))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def getFirtsMessage(self):
        self.cursor.execute("SELECT * FROM %s ORDER BY 'ID' LIMIT 1" % self.TabName)
        result = self.cursor.fetchone()
        data = {}
        data["content"] = result[1]
        data["auth"] = result[2]
        return data
        
pst = PyScripTalk()
pst.init()
print pst.test()
print pst.getFirtsMessage()

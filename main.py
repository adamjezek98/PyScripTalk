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
        self.cursor = self.db.cursor()

        

    def test(self):
        self.cursor.execute("SELECT * FROM %s " % self.TabName)
        return self.cursor.fetchall()

    def addMessage(self, messagetext, auth):
        try:
            self.cursor.execute("INSERT INTO %s (content, auth) VALUES ('%s', '%s') " % \
                                (self.TabName, messagetext, auth))
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

    def getMessages(self, count=1):
        self.cursor.execute("SELECT * FROM %s ORDER BY 'ID' LIMIT %s " % (self.TabName, count))
        result = self.cursor.fetchall()
        data = []
        for line in result:
            data.append({"content":line[1],"auth":line[2]})
        return data

    def getMessagesCount(self):
        self.cursor.execute("SELECT COUNT(*) FROM %s" % self.TabName)
        result = self.cursor.fetchone()
        return result[0]
        
        
pst = PyScripTalk()
pst.init()
print pst.getMessages(5)

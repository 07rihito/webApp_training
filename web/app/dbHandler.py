import os
import sys
#sys.path.append(os.path.abspath(".."))
#print(sys.path)
import pymysql, contextlib

from util.time import logMsg



class DBHandler:
  def __init__(self, host, port, user, password, db_name, cursor_mode='dict'):
    logMsg("start initialize")
    self.host = host
    self.port = port
    self.user = user
    self.password = password
    self.db = db_name
    self.conn = None
    if cursor_mode == "tuple":
      self.cursor_mode = pymysql.cursors.Cursor  # tuple
    elif cursor_mode == "dict":
      self.cursor_mode = pymysql.cursors.DictCursor  # dict
    else:
      print(f"{cursor_mode} is invalid to cursor mode.")
      return None
    logMsg("end initialize")
    logMsg("start connect to DB")
    try:
      self.conn = pymysql.connect(
        host=self.host,
        port=int(self.port),
        user=self.user,
        password=self.password,
        db=self.db,
        charset='utf8',
        cursorclass=self.cursor_mode
      )
      self.cursor = self.conn.cursor()
    except:
      logMsg("error occurred at db connection.")
    else:
      logMsg("db connection success")
    finally:
      logMsg("finally")
    #self.conn.close()


  def executeQuery(self):
    sql = "select * from userInfo;"
    self.cursor.execute(sql)
    #for test in self.cursor:
    #  print(test)
    result = self.cursor.fetchall()
    print(result)
    for res in result:
      print(res)

  def insert(self):
    sql = "INSERT INTO userInfo(id, username) VALUES(%s,%s);"
    tempId = self._getMinId()
    tempUser = f"sample{tempId}"
    logMsg(f"add record -> tempId: {tempId}, tempUser: {tempUser}")
    self.cursor.execute(sql, (tempId, tempUser))
    self.conn.commit()


  def _getMinId(self):
    self.cursor.execute("""
    SELECT MIN(a.id) + 1 AS id
    FROM userInfo a LEFT OUTER JOIN userInfo b
    ON a.id + 1 = b.id
    WHERE b.id IS NULL;
    """)
    result = self.cursor.fetchall()
    tempId = result[0]["id"]
    return tempId

  def __del__(self):
    print("instance delete")
    #print(self.conn)
    if self.conn:
      try:
        self.conn.close()
      except:
        print("error occurred at delete db connection. ")
      else:
        print("delete db connection is success. ")
    else:
      print("db connection doesn't exist. ")


if __name__ == "__main__":
  host = 'my-db-host'
  port = 3306
  user = 'root'
  password = 'RootPass'
  db_name = 'app'
  cursor_mode = "aaa"
  test = DBHandler(host,port,user,password,db_name)
  test.executeQuery()
  #test.insert()
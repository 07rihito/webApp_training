from application import db

class Users(db.Model):
  '''
  Users Table Model
  '''
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  passwd = db.Column(db.String(255))

#  def __init__(self, username, email, passwd):
#    self.username = username
#    self.email = email
#    self.passwd = passwd
    

#class Foods(db.Model):
#    '''
#    Food Table Model
#    '''
#    __tablename__ = 'foodlist'
#    
#    id = db.Column(db.Integer, primary_key=True)
#    eatdate = db.Column(db.Date)
#    foodname = db.Column(db.String(255))
#    fee = db.Column(db.Integer)
#    store = db.Column(db.String(255))
#    
#    def __init__(self, id, eatdate, foodname, fee, store):
#        self.id = id
#        self.eatdate = eatdate
#        self.foodname = foodname
#        self.fee = fee
#        self.store = store
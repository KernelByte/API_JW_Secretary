from models.Users import User as UserModel
from schemas.UserSchema import User as UserSchema
from schemas.UserSchemaUpdate import User as UserSchemaUpdate
import bcrypt 

class userService():
    def __init__(self,db) -> None:
        self.db = db

    def get_user(self, id):
      result = self.db.query(UserModel).filter(UserModel.idUser == id).first()
      return result

    def get_all_users(self):
      result = self.db.query(UserModel).all()
      return result
   
    def create_user(self, user: UserSchema):
       pwd = user.passwordUser.encode('utf-8')
       salt = bcrypt.gensalt()
       encript = bcrypt.hashpw(pwd,salt)
       user.passwordUser = encript.decode('utf-8')
       new_user = UserModel(**user.dict())
       self.db.add(new_user)
       self.db.commit()
       return

    def update_user(self, id: int, data: UserSchemaUpdate):
       update_user =  self.db.query(UserModel).filter(UserModel.idUser == id).first()
       update_user.nameUser = data.nameUser
       self.db.commit()
       return 
    
    def delete_user(self, id: int):
       self.db.query(UserModel).filter(UserModel.idUser == id).delete()
       self.db.commit()
       return 
    
    def get_user_email(self, email: str):
      result = self.db.query(UserModel).filter(UserModel.mailUser == email).first()
      return result
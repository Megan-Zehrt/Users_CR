#import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
   DB = 'users_schema'
   def __init__(self, data:dict):
      self.id = data['id']
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.email = data['email']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

      #Add additional columns from database here

   def info(self):
      returnStr = f"First Name = {self.first_name} || Last Name = {self.last_name} || Email = {self.email}"
      return returnStr

#CREATE
   @classmethod
   def create_one(cls, data:dict):
      query = "INSERT INTO users_schema.users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
      print("this is the model file")
      result = connectToMySQL(User.DB).query_db(query, data)
      print(data)
      return result
       
   # now we use the class methods to query our database

#READ
   @classmethod
   def get_all(cls) -> list:
      query = "SELECT * FROM users;"
      #make sure to call the connectToMySQL function with the schema you are targeting

      results = connectToMySQL(User.DB).query_db(query)
      #create an empty list to append our instances of users
      if not results:
         return []

      instance_list = []
      # iterate over the db results anad create instances of users with cls.
      for dictionary in results:
         instance_list.append(cls(dictionary))
      return instance_list
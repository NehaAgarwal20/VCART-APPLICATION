import pandas as pd 
import wrapper


'''
Wrapper function to connect ,commit and close a database connection
'''
def connect(query_function):
    import sqlite3


    def wrapper(*args,**kwargs):
        import sqlite3

        def wrapper(*args,**kwargs):
            con = sqlite3.connect("vcart.db")
            result = query_function(*args,**kwargs,con = con)
            con.commit()
            con.close()
            return result

    return wrapper  

  '''Get user information matching the username in a dictionary
  '''
  @connect
  def getUSerInfo(username,**kwargs):
      result = pd.read_sql(f"SELECT * FROM users WHERE username= '{username}'",**kwargs)        
      return result.to_dict('records')


'''
Register User
'''
@connect

def registerUser(username,password,**kwargs):
    con = kwargs.get("con",None)
    con.execute(

        '''
        INSERT INTO users(username,password)
        VALURES(?,?)
        ''',(username,password)

    )


















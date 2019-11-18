from datetime import datetime

import view
import controller
import model
import wrapper

'''
The main app entry point
'''

def app():
    ask = input(view.mainMenu()).strip()
    if ask == str(1):
        user = userLogin()
        userApp(user)

    elif ask == str(2):
        userRegistration()
    elif ask == str(3):
        print(veiw.printRoute("Quitting the application","The real world"))    
        return

    else:
        print(view.invalidString("Input", "Main Menu"))
        app()
    '''
    The login controller
    '''
    def userLogin():
        username=input(view.queryString("username"))
        password=input(view.queryString("password")) 
        user_info =model.getUserInfo(username)  
        if not user_info ==[]:
            if user_info[0]['password']==password:
                print(view.validString("Credentials",User Menu))
                return user_info[0]
            else:
                print(view.invalidString("Credentials","Main Menu"))
                app()
            else:
                print(view.invalidString("Credentials","Main Menu"))  
                app()
 

 '''Handling logout'''
    def user logout():
        view.printRoute("Logged you out", "main menu")
        app()

''' The Registration controller'''
    def userRegisteration():
        print(view.printTitle("Registration"))
        username=input(view.queryString("username"))
        if not model.getUserInfo("username","registration menu") )
        userRegistration()

        else:
            s


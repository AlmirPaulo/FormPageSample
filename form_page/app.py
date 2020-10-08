from browser import document as doc
from browser import alert

#'Have Letters' Function
def letters(tested_string):
    abc =  'qwertyuiopasdfghjklçzxcvbnm'
    if any(i in tested_string for i in abc) == True:
        return True
    elif any(i in tested_string for i in abc.upper()) == True:
        return True
    else:
        return False

#'Have numbers' Function
def numbers(tested_string):
    if any(i in tested_string for i in '1234567890') == True:
        return True
    else:
        return False

#'Have uppercase letters'Funcion
def big_letters(tested_string):
    abc =  'qwertyuiopasdfghjklçzxcvbnm'
    if any(i in tested_string for i in abc.upper()) == True:
        return True
    else:
        return False

#'Have lowercase letters' Function
def small_letters(tested_string):
    abc =  'qwertyuiopasdfghjklçzxcvbnm'
    if any(i in tested_string for i in abc) == True:
        return True
    else:
        return False

#Main Function
def validate(ev):
#First Name
    fn = doc['name1'].value
    if len(str((fn))) < 3:
        ev.preventDefault()
        alert('Fisrt Name is too short')

    elif numbers(fn) == True:
        ev.preventDefault()
        alert('Invalid First Name')
#Last Name
    ln = doc['name2'].value
    if len(str((ln))) < 3:
        ev.preventDefault()
        alert('Last Name is too short')

    elif numbers(ln) == True:
        ev.preventDefault()
        alert('Invalid Last Name')
#Username
    user = doc['user'].value
    if len(str((user))) < 3:
        ev.preventDefault()
        alert('Username is too short')

#Email
    email = doc['email'].value
    if '@' not in email:
        ev.preventDefault()
        alert('Email is invalid')
    elif '.' not in email:
        ev.preventDefault()
        alert('Email is invalid')

#Password
    passw = doc['pass'].value
    if len(passw) < 8:
        ev.preventDefault()
        alert('password is to short')
    elif small_letters(passw) == False:
        ev.preventDefault()
        alert('Passwords should have lowercase letters')
    elif big_letters(passw) == False:
        ev.preventDefault()
        alert('Passwords should have uppercase letters')
    elif numbers(passw) == False:
        ev.preventDefault()
        alert('Passwords should have numbers')


#Repeat Password
    passw_confirm = doc['pass_confirm'].value
    if passw_confirm != passw:
        ev.preventDefault()
        alert('The passwords do not match')

doc['form'].bind('submit', validate)



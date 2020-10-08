from browser import document as doc
from browser import alert, bind

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

#Main Function
def validate(ev):
#First Name
    fn = doc['name1'].value
    if len(str((fn))) < 3:
        ev.preventDefault()
        alert('too short')

    elif numbers(fn) == True:
        ev.preventDefault()
        alert('have numbers')


doc['form'].bind('submit', validate)

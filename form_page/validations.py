from browser import document as doc
from browser import alert
from browser.template import Template

err = False


#First Name validation
def err_name1(ev):
    fn = doc['name1'].value
    global err

    if len(str(fn)) > 2:
        pass

    else:
        alert('Invalid First Name')
        err = True

    if any(i in fn for i in '0123456789') == True:
         alert('Invalid First Name')
         err = True

doc['name1'].bind('blur', err_name1)

#Last Name validation
def err_name2(ev):
    ln = doc['name2'].value
    global err

    if len(str(ln)) > 2:
        pass
    else:
        alert('Invalid Last Name')
        err = True

    if any(i in ln for i in '0123456789') == True:
         alert('Invalid Last Name')
         err = True

doc['name2'].bind('blur', err_name2)

#Username validation
def err_user(ev):
    user = doc['user'].value
    global err

    if len(str(user)) > 2:
        pass
    else:
       err = True
       alert('Invalid Username')

doc['user'].bind('blur', err_user)

#Email validation
def err_email(ev):
    email = doc['email'].value
    global err

    if '@' not in email:
        err = True
        alert('Invalid Email')

    if '.' not in email:
        err = True
        alert('Invalid Email')

doc['email'].bind('blur', err_email)

#Password validation
def err_passw(ev):
    global err
    passw = doc['pass'].value
    num = '0123456789'
    abc = 'qwertyuiopasdfghjklçzxcvbnm'

    if len(passw) < 8:
        alert('Invalid Password: it should be at least 8 digits, alphanumerical, with upper and lowercase letters.')
        err = True

    if any(n in passw for n in num) == False:
        err = True
        alert('Invalid Password: it should be at least 8 digits, alphanumerical, with upper and lowercase letters.')


    if any(i in passw for i in abc) == False:
        err = True
        alert('Invalid Password: it should be at least 8 digits, alphanumerical, with upper and lowercase letters.')


    if any(i in passw for i in abc.upper()) == False:
        alert('Invalid Password: it should be at least 8 digits, alphanumerical, with upper and lowercase letters.')
        err = True

doc['pass'].bind('blur',err_passw)

#Repeat Passwords validation
def err_passw_confirm(ev):
    passw_confirm = doc['pass_confirm'].value
    passw = doc['pass'].value
    global err


    if passw_confirm != passw:
        err = True
        alert('Password not confirmated. Please repeat the same password in the correct fields.')

doc['pass_confirm'].bind('blur', err_passw_confirm)

#Validation não deu certo
def validation(ev):
    global err

    if  err == True:
        ev.preventDefault()
        alert('Some information is invalid')
        ev.stopPropagation()

doc['form'].bind('submit', validation)


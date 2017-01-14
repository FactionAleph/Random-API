import names
from random import *
def email():
    domains = ["@hotmail.com", "@gmail.com", "@aol.com", "@mail.com" , "@mail.kz", "@yahoo.com"]
    fn = names.get_first_name()
    ln = names.get_last_name()
    em = [fn+'.'+ln+choice(domains), str(randint(100,1000))+ln+choice(domains), fn+str(randint(100,200))+'.'+ln+choice(domains)]
    return em

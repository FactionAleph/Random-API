#new api (i just wanna make one with a different code lang) under development
import json, names
from random import Random
import copy
from faker import Factory
fake = Factory.create()

visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]
def completed_number(prefix, length):
    ccnumber = prefix
    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)
    sum = 0
    pos = 0
    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()
    while pos < length - 1:
        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9
        sum += odd
        if pos != (length - 2):
            sum += int(reversedCCnumber[pos + 1])
        pos += 2
    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
    ccnumber.append(str(checkdigit))
    return ''.join(ccnumber)
def credit_card_number(rnd, prefixList, length, howMany):
    result = []
    while len(result) < howMany:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))
    return result
generator = Random()
generator.seed()
visa16 = credit_card_number(generator, visaPrefixList, 16, 10)
cc = visa16[0].replace('.0','')
from random import *
domains = [ "@hotmail.com", "@gmail.com", "@aol.com", "@mail.com" , "@mail.kz", "@yahoo.com"]
n = '0000000000'
while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
    n = str(randint(10**9, 10**10-1))
num=(n[:3] + '-' + n[3:6] + '-' + n[6:])
data = {}
print('[')
for i in range(500):
    fn = names.get_first_name()
    ln = names.get_last_name()
    em = [fn+'.'+ln+choice(domains), str(randint(100,1000))+ln+choice(domains), fn+str(randint(100,200))+'.'+ln+choice(domains)]
    data['a-id'] = str(i)
    data['b-name'] = fn +' '+ ln
    data['d-addr'] = fake.address().replace('\n',' ')
    data['e-email'] = choice(em)
    data['c-age']  = str(randint(16,78))
    data['f-phone'] = num
    data['g-cc'] = cc
    data['h-friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
    json_data = json.dumps(data, sort_keys=True)
    print(json_data, ',')
fn = names.get_first_name()
ln = names.get_last_name()
em = [fn+'.'+ln+choice(domains), str(randint(100,1000))+ln+choice(domains), fn+str(randint(100,200))+'.'+ln+choice(domains)]
data['a-id'] = '500'
data['b-name'] = fn +' '+ ln
data['d-addr'] = fake.address().replace('\n',' ')
data['e-email'] = choice(em)
data['c-age']  = str(randint(16,78))
data['f-phone'] = num
data['g-cc'] = cc
data['h-friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
json_data = json.dumps(data, sort_keys=True)
print(json_data)

print(']')

'''
Example response:
  {
    "a-id": "0",
    "b-name": "Aundrea Hassell",
    "c-age": "23",
    "d-addr": "26821 Archer Walks Port Maxwellchester, UT 00596-2458",
    "e-email": "Aundrea.Hassell@mail.kz",
    "f-phone": "174-746-5352",
    "g-cc": "4486627783018130",
    "h-friends": [
      "Ruth Ramer",
      "David Bisarra",
      "Mary Waller"
    ]
  }
'''

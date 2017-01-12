#new api (i just wanna make one with a different code lang) under development
import json, names
from random import Random
import copy


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
import random
data = {}
print('[')
for i in range(99):
    data['id'] = str(i)
    data['name'] = names.get_full_name()
    data['age']  = random.randint(16,78)
    data['cc'] = cc
    data['friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
    json_data = json.dumps(data)
    print(json_data, ',')
data['id'] = '100'
data['name'] = names.get_full_name()
data['age']  = random.randint(16,78)
data['cc'] = cc
data['friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
json_data = json.dumps(data)
print(json_data)
print(']')
#Example output:
#  {
#    "name": "William Donaldson",
#    "cc": "4024007166090100",
#    "id": "0",
#    "age": 35,
#    "friends": [
#      "Jenna Cooper",
#      "Stuart Grimm",
#      "Yvette Scrivens"
#    ]
#  }

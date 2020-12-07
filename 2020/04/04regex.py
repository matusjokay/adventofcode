import re

opt = set(['cid'])
req = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

regex = dict()
regex['byr'] = '^(19[3-9][0-9]|192[0-9]|200[0-2])$'
regex['iyr'] = '^(201[0-9]|202[0-0])$'
regex['eyr'] = '^(202[0-9]|203[0-0])$'
regex['hgt'] = '^(1[6-8][0-9]cm|15[0-9]cm|19[0-3]cm|[6-6][0-9]in|5[9-9]in|7[0-6]in)$'
regex['hcl'] = '^(#[0-9a-fA-F]{6})$'
regex['ecl'] = '^(amb|b(lu|rn)|gr[yn]|hzl|oth)$'
regex['pid'] = '^([0-9]{9})$'
regex['cid'] = '^(.+)$'

def cntValid(restrict = None):
    passno = 0
    valid = 0
    req_tmp = set(req)
    opt_tmp = set(opt)
    for line in open('input.txt'):
        line = line.strip()

        if not line:
            passno += 1      
            if not req_tmp:
                valid += 1
            req_tmp = set(req)
            opt_tmp = set(opt)
        else:
            for word in line.split(' '):
                key, val = word.split(':')
                if restrict and not re.match(restrict[key], val):
                    continue                            
             
                if key in req_tmp:
                    req_tmp.remove(key)
                elif key in opt_tmp:
                    opt_tmp.remove(key)
                else:
                    print('key not found', key)
    return valid

print(cntValid())
print(cntValid(regex))

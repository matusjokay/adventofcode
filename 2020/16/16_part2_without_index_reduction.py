from functools import reduce


def read_input(fname):
    fields = dict()
    tickets = []
    
    state = 0
    for line in open(fname):
        line = line.strip()
        if not line:
            state += 1
            continue
        
        # read fields
        if state == 0:
            field, vals = line.split(': ')
            fields[field] = dict()
            fields[field]['ranges'] = []
            fields[field]['index'] = []
            vals = vals.split(' or ')
            for val in vals:
                start, end = val.split('-')
                fields[field]['ranges'].append(range(int(start), int(end)+1))
        # read your ticket
        elif state == 1:
            if line == 'your ticket:':
                continue
            my_ticket = [int(v) for v in line.split(',')]
        # read nearby tickets
        elif state == 2:
            if line == 'nearby tickets:':
                continue
            tickets.append([int(v) for v in line.split(',')])
            
    return fields, my_ticket, tickets


def main(fields, nearby_tickets, my_ticket):
    # create a set of all valid values
    valid_ranges = set()
    for val in fields.values():
        for v in val['ranges']:
            valid_ranges.update(set(v))

    # check the validity of tickets
    # 1) create a set of valid tickets
    # 2) sum error_rate of invalid values
    error_rate = 0
    valid_tickets = []
    for ticket in nearby_tickets + [my_ticket]:
        valid = True
        for val in ticket:
            if val not in valid_ranges:
                error_rate += val
                valid = False
                break
            
        if valid:
            valid_tickets.append(ticket)

    # part 1
    print(error_rate)


    # part 2

    # for values at first, second, third... position in data set
    for ind, field_vals in enumerate(zip(*valid_tickets)):
        # check if all values of a given position match some field criteria
        for field, ranges in fields.items():
            # list comprehension gives a non empty list, if the criteria don't match
            # if the criteria match, list is empty
            if not [False for v in field_vals if v not in ranges['ranges'][0] and v not in ranges['ranges'][1]]:
                # if criteria match, column index in data set is a candidate
                # there can be more than one, but only for one column
                # is valid that is only one value in the list `index`
                fields[field]['index'].append(ind)

    # sort fields by number of valid ranges in `index` candidates
    res = sorted([(len(vals['index'])-1,field,set(vals['index'])) for field,vals in fields.items()])
    # for each field extract its own index from `index` candidates
    res = {val[1]: list(val[2]-res[i-1][2])[0] if i>0 else list(val[2])[0] for i,val in enumerate(res)}
    # output product of all six fields on my ticket
    print(reduce(lambda x,y: x*y, [my_ticket[res[key]] for key in res.keys() if 'departure' in key], None))


fields, my_ticket, nearby_tickets = read_input('in2.txt')
main(fields, nearby_tickets, my_ticket)

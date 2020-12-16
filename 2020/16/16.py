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

    fields_identified = dict()
    # while there is one data field with only one value in the `index` cadidate
    # that index identifies a given data field in the input data set
    f = [(field,vals['index'][0]) for field,vals in fields.items() if len(vals['index']) == 1]
    while f:
        # set index for a given data field
        fields_identified[f[0][0]] = f[0][1]
        # remove used index from all field's `index` candidates
        [k['index'].remove(f[0][1]) for k in fields.values() if f[0][1] in k['index']]
        # next iteration - search another field with only one value in `index` list
        f = [(field,vals['index'][0]) for field,vals in fields.items() if len(vals['index']) == 1]

    # output product of all six fields on my ticket
    print(reduce(lambda x,y: x*y, [my_ticket[fields_identified[key]] for key in fields_identified.keys() if 'departure' in key]))


fields, my_ticket, nearby_tickets = read_input('input.txt')
main(fields, nearby_tickets, my_ticket)

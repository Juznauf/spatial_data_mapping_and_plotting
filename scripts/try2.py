
district_names = []
with open('d_list.csv', encoding='utf8') as in_file:
    counter = 0
    for line in in_file:
        line = line.rstrip('\n')
        if counter == 0:
            pass
        else:
            line = line.lstrip('"').rstrip('"').split(',') 
            new_line = ' '.join(line[0].split(' ')[:2])
            # print(line[0].split(' ')[:2])
            district_names.append(new_line)
        counter += 1                


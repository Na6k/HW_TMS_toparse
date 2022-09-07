import json    

def to_parse_csv(): # It's function parsing .csv file
    f = open('to_parse.csv', 'r') 
    lines = [line.rstrip() for line in f] # rstrip() delet /n in the end str
    results = []
    for line in lines:
        words = line.split(',')

        results.append(
            (words[0],words[1],words[2])
                        )

    keys = results[0]
    val1 = results[1]
    val2 = results[2]
    a1 = list(zip(keys, val1))
    a2 = list(zip(keys, val2))
    lst = []
    lst.append(dict(a1))
    lst.append(dict(a2))
    f.close()
    return lst


def show(parse=None): # It's function to print result
    print('{}'.format(parse))


def save_to_json(saving=None): #It's function save this result in file .json format 
    with open('save_to_parse.json', 'w') as file_json:
        json.dump(saving, file_json)


def main():
    parse_csv = to_parse_csv()
    show(parse = parse_csv)
    save_to_json(saving = parse_csv)

if __name__=='__main__':
    main()    




import json   


def to_parse_csv(): # It's function parsing .csv file
    with open('to_parse.csv', 'r') as f: 
        head = f.readline().strip().split(',') # strip() delet /n in the end str, split() separation string sep=','
        res = [dict(zip(head, line.strip().split(','))) for line in f] 
    return res


def show(parse=None): # It's function to print result
    print('{}'.format(parse))


def save_to_json(saving=None): #It's function save this result in file .json format 
    with open('save_to_parse.json', 'w' ) as file_json:
        json.dump(saving, file_json, indent=4)


def main():
    parse_csv = to_parse_csv()
    show(parse = parse_csv)
    save_to_json(saving = parse_csv)

if __name__=='__main__':
    main()    




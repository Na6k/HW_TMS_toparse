import json
from textwrap import indent    

def to_parse_csv(): # It's function parsing .csv file
    with open('to_parse.csv', 'r') as f: 
        lines = [line.rstrip() for line in f] # rstrip() delet /n in the end str

    results = []
    for line in lines:
        words = line.split(',')

        results.append(
            (words[0],words[1],words[2])
                        )    
    ls = []
    for i in range(1,len(results)):
        keys = results[0]
        val = results[i]
        a = list(zip(keys, val))
        ls.append(dict(a))
    return ls


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




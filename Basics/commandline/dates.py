import argparse
import datetime

parser = argparse.ArgumentParser("Returns age of a person")
parser.add_argument('-f', '--first', help='specify first name', type=str, required=True, dest="first_name")
parser.add_argument('-l', '--last', help="last name", type=str, required=False, dest="last_name")
parser.add_argument('-y', '--year', help="Year of birth", type=int, required = False, dest="birth_year")

args = parser.parse_args()

if args.first_name:
    names = [args.first_name]
    if args.last_name:
        names.append(args.last_name)

fullname = ' '.join(names)

current_date_year = datetime.datetime.utcnow().year
age = current_date_year - args.birth_year  
print(f'{fullname} is {age} years old ')

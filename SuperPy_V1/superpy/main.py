# Imports
import argparse
import csv
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

from functions import date_type
#import datetime


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
#find current day with fomate:year-month-day
current_day=date.today()
print(current_day)

#currentday plus two days works ? yes
currentDay_plus2Day =current_day +timedelta(2)
print('currentDay_plus2Day:',currentDay_plus2Day)




#hieronder :module argparse/for buy

buy_parser=argparse.ArgumentParser(description="report inventory --now ??")
buy_parser.add_argument("--product_name", type=str, help="give the name of the product choice:apple, banana, manderin") #works?y 
buy_parser.add_argument("--price", type=float, help="give the price of the product choice: ???")#works? yes 
buy_parser.add_argument("--expiration_date", type=date_type, help="Enter the expiredate in 'year-month-day'format")#works ?

buy_args=buy_parser.parse_args()
print('r44',buy_args.product_name)
print('r45',buy_args.price)
print('r46,',buy_args.expiration_date)


def main():
    pass


if __name__ == "__main__":
    main()

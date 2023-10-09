from datetime import datetime

import argparse

def date_type(date_string,):
    try:
        date_object=datetime.strptime(date_string,'%Y-%m-%d')
        formated_date_object=date_object.strftime('%Y-%m-%d')
        return formated_date_object
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use 'year-month-day' (e.g.,'2023-10-15).")

#hieronder test result of date_type w?? yes good job
#result_date_type=date_type("2023-01-02")
#print("In function.py:result_date_type",result_date_type )
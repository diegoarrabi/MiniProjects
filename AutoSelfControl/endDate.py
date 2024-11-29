#!/usr/bin/python3

from datetime import datetime
from datetime import timedelta


def main():

    #! CHANGE ONCE SCRIPT IS DONE
    ### this is set, but due to a bug, the time tha actually gets set is whatever is selected on the slider
    modified_date = datetime.today() + timedelta(days=6, hours=23)
    
    modified_date = modified_date.replace(second=0, microsecond=0).isoformat()
    
if __name__ == '__main__':
    main()
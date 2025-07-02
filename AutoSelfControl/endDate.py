#!/usr/bin/python3

from sys import argv
from datetime import datetime
from datetime import timedelta
from datetime import timezone


def main(_arg):

    _arg = _arg or ['1']

    #! CHANGE ONCE SCRIPT IS DONE
    today_date = datetime.now(timezone.utc).replace(microsecond=0)

    modified_date = today_date + timedelta(days=0, hours=0, minutes=2)
    modified_date = modified_date.isoformat()

    # print(modified_date)
    if _arg[0] == '1':
        print(today_date)
    else:
        print(modified_date)


if __name__ == '__main__':
    main(argv[1:])

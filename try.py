import datetime
import os
from datetime import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w'):

        timestamp = os.path.getmtime(filename)
        date = datetime.fromtimestamp(timestamp).date()
    # Convert the timestamp into a readable format, then into a string

    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(date))


print(file_date("newfile.txt"))

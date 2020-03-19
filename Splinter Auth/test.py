import re
import string

dob_format = re.compile('(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d')
email_format = re.compile('(\d|[a-zA-Z])*\@(\d|[a-zA-Z])*\.(\d|[a-zA-Z])*')

print(string.ascii_letters + '-')


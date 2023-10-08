# condition
# 1 a-z
# 2 ".""_" time
# 3 "@" time 1
# 4 "." last to 2 and 3 position
import re
email = "kumar@gmail.com"
email_condition  = "[.]\w{2,3}$?"

if re.search(email_condition,email):
    print("ok")

else:
    print("not ok")


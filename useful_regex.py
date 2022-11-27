import re

# regex for password
# 8 char | uppercase | lowercase | number | symbol
input_password = input("Enter your Password: ")
if re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', input_password):
    print('Valid password!')
else:
    print('Invalid Password!')


# regex for email validation
email = input("Email address: ")
if re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', email):
    print("This is a valid email address.")
else:
    print("The email address (", email, ") is not a valid email address.")


# regex for URL validation
urlList = ['https://www.google.com:80', 'http://yahoo.com', 'ftp://modevelops.org', 'https://www.some-website.domain' , 'https://bbhosted.cuny.edu', 'hello@sometext.come', 'http://www.microsoft.com/user/login/121']
for url in urlList:
  url_match = re.search(r'^(http|https|ftp):\/\/([\w.-]+).([\w]+)([:0-9]?)([\/\w]+)', url)
  if (url_match):
    print('Valid URL: ', url_match.group())
  else:
    print('Invaild URL: ', url)




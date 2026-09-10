import os
import re
import urllib.parse

CLINT_EMAIL =os.getnev("CLIENT_EMAIL","")

KEYWORDS = (
  "gmail", "email","e-mail","mail",
  "write an email", "write mail","sent mail","draft mail",
  "compose an email","write mail","send mail","draft mail",
  "compose mail"

)
def is_email_command(text):
  text =text.lower()
  return any(k in text for k in KEYWORDS)

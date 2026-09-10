import os
import jason
import re
import time
import random
import urllib.request
import urllib.error

API_KEY =os.getenv("GEMINI_API_KEY","")
MODEL = os.getnev("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEYis missing.")

prompt =f"""
you are a professional Gmail email writing assistant.

convert the user's voice command into a professional email.

Rules:
-Do not copy the command literally
-Do not explain anything.
-Do not invert names,dates,prices,companies,attachments,or facts.
-Keep the email natural and concise.
-Include an appropriate greeting and closing.

output exactly:

SUBJECT: <subject>
BODY:
<email body>

User command:
(command)
"""

url= (
  f"https://generativelanguage.googleapis.com/"
  f"vlbeta/models/{MODEL}:generateContent"
)

payload = {
  "contents":[{"parts":[{"text": prompt}]}],
  "generationconfig": {
    "temperature":0.7,
    "maxOutputTokens":800
  }
}

req=urllib.request.Request(
  url,
  data=json.dumps(payload).encod(),
  headers={
    "content-type":"application/json",
    "x-goog-api-key": API_KEY
    },
    methods="POST"
)

for attempt in range(4):
  try:
    with urllib.request.urlopen(req,timeout=30) as response:

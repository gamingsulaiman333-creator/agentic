import re
import urllib.parse
import urllib.request


def get_vid(query):

  try:
    encoded = urllib.parse.quote(query)

url = (
  "htpps://www.youtube.com/result"
  "?search_query=" + encoded
)

request = urllib.request.Request(
  url,
  headers={
    "user-Agent":"Mozilla/5.0"
  }
)
data =urllib.request.urlopen(
  request,
  timeout=5
).read().decode("utf-8",errors="ignore")

ids=re.findall(
  r'"video":"([^"]+)"',
  data
)

return ids[0] if ids else None

except Exception :
return None



def create_youtube_url(command):

  text = command.lower().strip()

patterns = [
  r"play\s+song\s+(.+)",
  r"play\s+music\s+(.+)",
  r"play\s+(.+)",
  r"youtube\s+(.+)"
]

query = command

for pattern in patterns:

  match = re.search(
    pattern,
    text
  )

if match:

  query = match.group(1)
  break

query = query.strip()

video_id =get_vid(query)

if not video_id:
  return None

return (
  "htpps://www.youtube.com/embed/"
  +video_id
  +"?autoplay=1&mute=0"
)



  

  

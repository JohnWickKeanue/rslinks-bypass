import requests

url = "https://rslinks.net/ds9ux2oe"

def rs(url):
      client = requests.session()
      download = get(url, stream=True, allow_redirects=False)
      v = download.headers["location"]
      code = v.split('ms9')[-1]
      final = f"http://techyproio.blogspot.com/p/short.html?{code}=="
      return final
      
print(rs(url))


import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.alcom.info/users/fashion/swarovski/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    
with open('alcom_swarovski.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Downloaded alcom_swarovski.html")

import re
import requests

def get_subheadings(url):
    response=requests.get(url)
    html_content=response.text

    pattern=r'<h3[^>]*>(.*?)</h3>'
    #[^>]*-любой символ кроме >
    #.*?-идут любые символы
    
    subheadings=re.findall(pattern, html_content)

    subheadings= [re.sub(r'id=\".*?\"', '', subheading) for subheading in subheadings]

    return subheadings

url="http://www.columbia.edu/~fdc/sample.html"

res=get_subheadings(url)
print(res)
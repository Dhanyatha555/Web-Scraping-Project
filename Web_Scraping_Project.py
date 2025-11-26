import requests
from bs4 import BeautifulSoup

def scrape_python_blog_titles():
    url = 'https://blog.python.org'

    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('h3', class_='post-title')
        print("\nLatest Blog Titles from Python.org:\n")


        for i, title in enumerate(titles, 1):
            text = title.get_text(strip=True)
            print(f"{i}. {text}")


    except requests.exceptions.RequestException as e:
        print("Error fetching the blog:", e)

scrape_python_blog_titles()

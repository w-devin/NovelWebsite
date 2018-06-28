import requests
import os
from bs4 import BeautifulSoup


def get_chapter(url):
    book_num = url.split('/')[-1].split('.')[0]
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    chapter_block = soup.find('div', attrs={'id': 'chapterlist'})
    chapter = chapter_block.find_all('a')
    if not os.path.exists('static/book/%s.txt' %book_num):
        with open('static/book/%s.txt' %book_num, 'w', encoding='utf8') as f:
            for c in chapter[1:]:    
                f.write(",".join([c.get('href'), c.string]) + '\n')
        return 'static/book/%s.txt' %book_num
    return 'static/book/%s.txt' %book_num


def get_chapter_content(url):
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    title = soup.find('span', attrs={"class": "title"}).text
    chapter_content = soup.find('div', attrs={"id": "chaptercontent"}).text.replace('『章节错误,点此举报』', '')
    chapter_content = chapter_content.replace('　　　　', '<br>')
    return chapter_content, title

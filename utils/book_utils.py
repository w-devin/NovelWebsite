#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-06-28 15:28
# @Author: Binyou
# @Site: 
# @File: book_utils.py

import requests
import os
from bs4 import BeautifulSoup


def get_chapter_list(book_path):
    print(book_path)
    with open(book_path, 'r', encoding='utf8') as f:
        chapter = list()
        for line in f.readlines():
            chapter.append(line.split(','))
        return chapter



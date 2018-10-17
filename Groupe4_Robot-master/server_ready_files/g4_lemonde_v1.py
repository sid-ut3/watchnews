#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:10:36 2018

@author: Nabil Hbabou
"""

import datetime as date
import re

import requests
import unidecode
from bs4 import BeautifulSoup

import g4_utils_v33 as utilsg4


def linkRSS(url_rss_lib):
    rss_list = []
    link_rss = []
    req = requests.get(url_rss_lib)
    data = req.text
    soup = BeautifulSoup(data, "lxml")
    rss_items = soup.find_all("tr")
    # Flux RSS
    for ri in rss_items:
        rss_list.append(ri.a.get('href'))
    for rl in rss_list:
        req = requests.get(rl)
        dt = req.text
        sp = BeautifulSoup(dt, "lxml")
        item = sp.find_all('item')
        # Récuperer le lien des articles
        for i in item:
            link_rss.append(re.search(r"<link/>(.*)", str(i)).group(1))
    return link_rss


def info_articles(article_link):
    req = requests.get(article_link)
    data = req.text
    soup = BeautifulSoup(data, "lxml")

    title = unidecode.unidecode(soup.find('title').string)

    newspaper = "Le Monde"

    # Article theme
    if(soup.find("li", class_="ariane z2")):
        theme = soup.find("li", class_="ariane z2").find("a").get_text()
    else:
        theme = 'Forum'

    # Author of the article
    if(soup.find("span", class_="auteur")):
        if(soup.find("span", class_="auteur").a):
            author = soup.find("span", class_="auteur").find("a").get_text()
        else:
            author = soup.find("span", class_="auteur").get_text()
        author = re.sub(r"\s\s+", " ", author)
        author = re.sub(r"^ ", "", author)
    else:
        author = ""

    # publication date
    da = re.search(r"\d{4}-\d{2}\-\d{2}", soup.find("time").get("datetime"))[0]
    if(da):
        date_p = date.datetime.strptime(da, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        date_p = str(date.datetime.now().strftime("%d/%m/%Y"))

    # Article content
    content = ""
    for div in soup.find_all('div'):
        for p in div.find_all('p'):
            content += p.get_text() + " "
    content = unidecode.unidecode(re.sub(r"\s\s+", " ", content))

    new_article = utilsg4.recovery_article(
        title, newspaper, [author], date_p, content, theme)

    return new_article


def recent(url):
    rubriques = []
    links = []
    actualite = []
    req = requests.get(url)
    data = unidecode.unidecode(req.text)
    soup = BeautifulSoup(data, "lxml")
    # En ce moment
    for nav in soup.find_all('nav', id="en_ce_moment"):
        for nv in nav.find_all("a"):
            actualite.append(url + nv.get("href"))
    # Recuperation des articles qui sont en ce moment
    for act in actualite:
        req = requests.get(act)
        data = unidecode.unidecode(req.text)
        soup = BeautifulSoup(data, "lxml")
        for h in soup.find_all('h3'):
            for lien in h.find_all('a'):
                links.append(url + lien.get('href'))
    # Rubriques
    for nav in soup.find_all('nav', id="navigation-generale"):
        for nv in nav.find_all("a"):
            rubriques.append(url + nv.get("href"))
            rubriques = rubriques[1:]
    # Recuperation des articles des differents rubriques
    for rub in rubriques:
        req1 = requests.get(rub)
        data1 = unidecode.unidecode(req1.text)
        soup1 = BeautifulSoup(data1, "lxml")
        for art in soup1.find_all('article'):
            for lien in art.find_all('a'):
                links.append(url + lien.get('href'))
    return links


def recuperation_info_lmde(
        file_target="data/clean/robot/" + str(date.datetime.now().date()) + "/"):
    source = "lemonde/"
    url_rss_lib = "http://www.lemonde.fr/rss/"
    abbreviation = "lmde"
    url = "http://www.lemonde.fr"

    list_articles = []
    i = 0

    listRSS = linkRSS(url_rss_lib)
    for article_link in listRSS:
        if "/article/" in article_link:
            i += 1
            list_articles.append(info_articles(article_link))

            if i == 20:
                utilsg4.create_json(
                    file_target, list_articles, source, abbreviation)
                i = 0
                list_articles = []

    # links = recent(url)
    # list_articles.extend(articlesList(links))
    utilsg4.create_json(file_target, list_articles, source, abbreviation)


if __name__ == '__main__':
    recuperation_info_lmde()

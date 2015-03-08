#!/usr/bin/env python
# encoding: utf-8

class Scraper(object):

    def get_link_from_linktext_in_divclass(self, html, divclass, linktext):
        div_html = self.get_html_with_divclass(html, divclass)

        link = div_html.find('a', href=True, text=linktext)
        return link['href']

    def get_html_with_divclass(self, html, divclass):
        div_html =  html.find('div', attrs={
            'class': divclass
        })

        return div_html

    def get_text_from_taged_item(self, html, tag):
        tagged_html = html.select(tag)

        texts = []
        for tag in tagged_html:
            texts.append(tag.get_text())

        return texts
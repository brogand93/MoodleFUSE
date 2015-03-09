#!/usr/bin/env python
# encoding: utf-8

class Scraper(object):

    def get_link_from_linktext_in_divclass(self, html, divclass, linktext):
        div_html = self.get_html_with_divclass(html, divclass)

        link = div_html.find('a', href=True, text=linktext)
        if link is not None:
            return link['href']
        return link

    def get_html_with_divclass(self, html, classname):
        return self._get_html_from_tag_label_with_name(html, 'div', 'class', classname)

    def get_html_items_with_spanclass(self, html, classname):
        return self._get_all_html_from_tag_label_with_name(html, 'span', 'class', classname)

    def get_html_with_liarialabel(self, html, labelname):
        return self._get_html_from_tag_label_with_name(html, 'li', 'aria-label', labelname)

    def get_instances_from_span_list_with_type(self, spanlist, type):
        instances = []

        for span_item in spanlist:
            sections = span_item.get_text().split(" ")
            if sections[1] == type:
                instances.append(sections[0])

        return instances

    def _get_html_from_tag_label_with_name(self, html, tag, label, name):
        if html is None:
            return None

        html = html.find(tag, attrs={
            label: name
        })

        return html

    def _get_all_html_from_tag_label_with_name(self, html, tag, label, name):
        if html is None:
            return None

        html = html.findAll(tag, attrs={
            label: name
        })

        return html


    def get_text_from_taged_item(self, html, tag):
        tagged_html = html.select(tag)

        texts = []
        for tag in tagged_html:
            texts.append(tag.get_text())

        return texts
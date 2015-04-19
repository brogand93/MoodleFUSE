#!/usr/bin/env python
# encoding: utf-8

"""Class to scrape Moodle HTML, looking for specific
   information.
"""

from moodlefuse.moodle import attributes


class Scraper(object):

    def get_link_from_linktext_in_divclass(self, html, divclass, linktext):
        div_html = self.get_html_with_divclass(html, divclass)
        return self.get_link_from_linktext(div_html, linktext)

    def get_link_from_linktext(self, html, linktext):
        link = html.find(attributes.LINK, href=True, text=linktext)

        if link is not None:
            return link[attributes.LINKTEXT]

        return link

    def get_html_with_divclass(self, html, classname):
        return self._get_html_from_tag_label_with_name(
            html, attributes.DIV,
            attributes.CLASS, classname
        )

    def get_html_items_with_divclass(self, html, classname):
        return self._get_all_html_from_tag_label_with_name(
            html, attributes.DIV,
            attributes.CLASS, classname
        )

    def get_html_with_aclass(self, html, classname):
        return self._get_html_from_tag_label_with_name(
            html, attributes.LINK,
            attributes.CLASS, classname
        )

    def get_all_html_with_atitle(self, html, titlename):
        return self._get_all_html_from_tag_label_with_name(
            html, attributes.LINK,
            attributes.TITLE, titlename
        )

    def get_html_items_with_tdclass(self, html, classname):
        return self._get_all_html_from_tag_label_with_name(
            html, attributes.TABLE,
            attributes.CLASS, classname
        )

    def get_html_items_with_spanclass(self, html, classname):
        return self._get_all_html_from_tag_label_with_name(
            html, attributes.SPAN,
            attributes.CLASS, classname
        )

    def get_html_with_liarialabel(self, html, labelname):
        return self._get_html_from_tag_label_with_name(
            html, attributes.LIST,
            attributes.LABEL, labelname
        )

    def get_instances_from_span_list(self, span_list):
        instances = []

        for span_item in span_list:
            sections = span_item.get_text().split(" ")
            instances.append(sections[0])

        return instances

    def get_link_from_span_list_with_type_and_name(self, spanlist, instance_type, name):
        for span_item in spanlist:
            sections = span_item.get_text().split(" ")
            if sections[1] == instance_type and sections[0] == name:
                return span_item.find(attributes.LINK, href=True)[attributes.LINKTEXT]

        return None

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

    def get_text_from_html_list(self, html_list):
        texts = []
        for item in html_list:
            texts.append(item.get_text())

        return texts

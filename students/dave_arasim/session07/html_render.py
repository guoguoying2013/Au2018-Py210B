#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

############################################################
# This is the framework for the base class
############################################################

class Element(object):
    tag = 'html'
    doctype = ''
    indent_level = 0
    indent_str = '   '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attrs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        nv_pairs = ''

        if self.attrs is not None:
            for key,value in self.attrs.items():
                nv_pairs += ' ' + str(key) + '='
                nv_pairs += '"' + str(value) + '"'

        return "<{}{}>".format(self.tag, nv_pairs)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file):
        if self.doctype != '':
            out_file.write(self.doctype)
        out_file.write(Element.indent_str * Element.indent_level)
        out_file.write(self._open_tag())
        out_file.write("\n")

        Element.indent_level += 1

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(Element.indent_str * Element.indent_level)
                out_file.write(content)
                out_file.write('\n')

        Element.indent_level -= 1
        if Element.indent_level < 0:
            Element.indent_level = 0

        out_file.write(Element.indent_str * Element.indent_level)
        out_file.write(self._close_tag())
        out_file.write("\n")


class Html(Element):
    tag = 'html'
    doctype = '<!DOCTYPE html>\n'


class Head(Element):
    tag = 'head'


class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class List(Element):
    tag = 'li'


class UList(Element):
    tag = 'ul'


############################################################
# This is the framework for the 'one line tag' subclass
############################################################

class OneLineTag(Element):
    def append(self, *args):
        raise NotImplementedError("You can not append content to a OneLineTag")

    def render(self, out_file):
        out_file.write(super().indent_str * super().indent_level)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write("\n")


class Title(OneLineTag):
    tag = 'title'


class Anchor(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link

        super().__init__(content, **kwargs)


class Header(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(level)

        super().__init__(content, **kwargs)


############################################################
# This is the framework for the 'self close tag' subclass
############################################################

class SelfCloseTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfCloseTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfCloseTag")

    def _open_tag(self):
        nv_pairs = ''

        if self.attrs is not None:
            for key,value in self.attrs.items():
                nv_pairs += ' ' + str(key) + '='
                nv_pairs += '"' + str(value) + '"'

        return "<{}{}".format(self.tag, nv_pairs)

    def render(self, out_file):
        tag = self._open_tag() + " />\n"
        out_file.write(super().indent_str * super().indent_level)
        out_file.write(tag)


class Hr(SelfCloseTag):
    tag = 'hr'


class Br(SelfCloseTag):
    tag = 'br'


class Meta(SelfCloseTag):
    tag = 'meta'
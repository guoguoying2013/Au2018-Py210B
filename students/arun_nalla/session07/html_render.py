#!/usr/bin/env python3

"""
A class-based system for rendering html.

By Arun Nalla 11-30-2018
"""

# This is the framework for the base class

class Element(object):
    tag = "html"
    indent = '   '


    def __init__(self, content=None, **kwargs):
        self.contents = []
        if content is not None:
            self.contents = [content]
        self.kwargs = kwargs


    def append(self, new_content):
        self.contents.append(new_content)


    def attributes(self):
        attribute = ''
        for key, value in self.kwargs.items():
            attribute += ' {}="{}"'.format(key, value)
        return attribute


    def _open_tag(self):
        open_tag = '<{}{}>'.format(self.tag, self.attributes())
        return open_tag


    def _close_tag(self):
        close_tag = '</{}>'.format(self.tag)
        return close_tag


    def render(self, out_file, cur_ind = ''):
        out_file.write(cur_ind)
        out_file.write (self._open_tag())
        out_file.write('\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind+self.indent)
            except AttributeError:
                out_file.write(cur_ind+self.indent)
                out_file.write(content)
            out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())


class Html(Element):

    def render(self, out_file):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file)


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    tag = 'title'

    def append(self, content):  
        raise NotImplementedError

    def render(self, out_file, cur_ind = ''):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):

    def __init__ (self, content = None, **kwargs):
        if content is not None:
            raise TypeError ('Cannot have content')
        super().__init__(content=content, **kwargs)

    def _open_tag(self, cur_ind = ''):
        open_tag = '<{}{}/>'.format(self.tag, self.attributes())
        return cur_ind + open_tag

    def render(self, outfile, cur_ind = ''):
        open_tag = '<{}{}/>'.format(self.tag, self.attributes())
        outfile.write(cur_ind)
        outfile.write(open_tag)


    def append(self, *args):
        raise TypeError ('Cannot add content')


class Hr (SelfClosingTag):
    tag = 'hr'

class Br (SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content = None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Li(Element):
    tag = 'li'

class Ul(Element):
    tag = 'Ul'

class H(OneLineTag):

    def __init__(self, level, content = None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content, **kwargs)

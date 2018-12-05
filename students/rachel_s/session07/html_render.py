#!/usr/bin/env python3

from string import Template

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.contents = []
        self.args = ''
        if content:
            self.contents.append(content)
        if kwargs:
            self.args = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _indenter(self, cur_ind):
        output = ''
        for i in range(cur_ind):
            output += self.indent
        return output

    def render(self, out_file, cur_ind=0):
        out_file.write(self._indenter(cur_ind))
        out_file.write(self._open_tag())
        out_file.write('\n')
        for item in self.contents:
            try:
                item.render(out_file, cur_ind=cur_ind+1)
            except AttributeError:
                out_file.write(self._indenter(cur_ind+1))
                out_file.write(item)
            out_file.write("\n")
        out_file.write(self._indenter(cur_ind))
        out_file.write(self._close_tag())

    def _unpack_kwargs(self):
        output = ''
        for key, value in self.args.items():
            output += ' {par}=\"{val}\"'.format(par=key, 
            val=str(value))
        return output

    def _open_tag(self):
        output = ''
        output += '<{}'.format(self.tag)
        if self.args:
            output += self._unpack_kwargs()
        output += '>'
        return output

    def _close_tag(self):
        return('</{}>'.format(self.tag))


class Html(Element):
    def render(self, out_file, cur_ind=0):
        out_file.write(self._indenter(cur_ind))
        out_file.write('<!DOCTYPE html>\n')
        out_file.write(self._indenter(cur_ind))
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

    def render(self, out_file, cur_ind=0):
        out_file.write(self._indenter(cur_ind))
        out_file.write(self._open_tag())
        for item in self.contents:
            out_file.write(item)
        out_file.write(self._close_tag())


class Title(OneLineTag):
    pass


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def _open_tag(self):
        output = ''
        output += '<{}'.format(self.tag)
        if self.args:
            output += self._unpack_kwargs()
        output += ' />'
        return output
    
    def _close_tag(self):
        return ''
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(str(level))
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'
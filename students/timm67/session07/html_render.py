#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    _doctype = '<!DOCTYPE html>'
    _tag = 'html'
    indent = '    '
    _attributes = {}

    def __init__(self, content_in=None, **kwargs):
        if content_in is not None:
            self._content = [content_in]
        else:
            self._content = []

        # save attributes passed in as kwargs
        if len(kwargs.items()) > 0:
            for key, value in kwargs.items():
                self._attributes[key] = value
        else:
            self._attributes = {}

    def append(self, new_content):
        if new_content is not None:
            self._content.append(new_content)

    def render_attributes(self, out_fd, indent_in):
        num_attrib = len(self._attributes)
        if(num_attrib > 0):
            out_fd.write('{0}<{1} '.format(indent_in, self._tag))
            for key, value in self._attributes.items():
                out_fd.write('{0}="{1}" '.format(key, value))
        else:
            out_fd.write('{0}<{1}>'.format(indent_in, self._tag))
        return num_attrib

    def render(self, out_fd, indent_in=''):
        try:
            # render DOCTYPE
            if isinstance(self, Html) is True:
                out_fd.write('{0}\n'.format(self._doctype))

            num_attr = self.render_attributes(out_fd, indent_in)
            if (num_attr > 0):
                out_fd.write('>\n')
            else:
                out_fd.write('\n')

            # loop through the list of contents:
            for content_item in self._content:
                try:
                    content_item.render(out_fd, (indent_in + self.indent))
                except AttributeError:
                    out_fd.write('{0}{1}\n'.format(indent_in + self.indent,
                                                   content_item))
            out_fd.write('{0}</{1}>\n'.format(indent_in, self._tag))
        except IOError:
            print("Element: I/O Error on render")
            return


class OneLineTag(Element):
    _attributes = {}

    def append(self, content_in):
        raise NotImplementedError

    def render(self, out_fd, indent_in=''):
        try:
            num_attrib = self.render_attributes(out_fd, indent_in)

            # if isinstance(self._content[0], str):
            #     out_fd.write('{0}{1}\n'.format(indent_in + self.indent,
            #                   self._content[0]))
            # else:
            #     self._content[0].render(out_fd, (indent_in + self.indent))
            if self._content[0] is not None:
                if num_attrib > 0:
                    out_fd.write('>')
                out_fd.write('{0}'.format(self._content[0]))
                out_fd.write('</{0}>\n'.format(self._tag))
            else:
                if num_attrib > 0:
                    out_fd.write('>')

        except IOError:
            print("OneLineTag: I/O Error on render")
            return


class SelfClosingTag(Element):
    _attributes = {}

    def __init__(self, content_in=None, **kwargs):
        if content_in is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super(SelfClosingTag, self).__init__(content_in, **kwargs)

    def append(self, content):
        raise TypeError("You can't add to a self closing tag")

    def render_attributes(self, out_fd, indent_in):
        num_attrib = len(self._attributes)
        if(num_attrib > 0):
            out_fd.write('{0}<{1} '.format(indent_in, self._tag))
            for key, value in self._attributes.items():
                out_fd.write('{0}="{1}" '.format(key, value))
        else:
            out_fd.write('{0}<{1} '.format(indent_in, self._tag))
        return num_attrib

    def render(self, out_fd, indent_in=''):
        try:
            self.render_attributes(out_fd, indent_in)
            if self._content is not None:
                for content_item in self._content:
                    if isinstance(content_item, str):
                        out_fd.write('{0}{1}\n'.format(indent_in + self.indent,
                                                       content_item))
                out_fd.write('/>\n')
        except IOError:
            print("SelfClosingTag: I/O Error on render")
            return


class Html(Element):
    _tag = 'html'
    _attributes = {}


class Head(Element):
    _tag = 'head'
    _attributes = {}


class Body(Element):
    _tag = 'body'
    _attributes = {}


class P(Element):
    _tag = 'p'
    _attributes = {}


class Title(OneLineTag):
    _tag = 'title'
    _attributes = {}


class Hr(SelfClosingTag):
    _tag = 'hr'
    _attributes = {}


class H(OneLineTag):
    _tag = 'h'
    _attributes = {}

    def __init__(self, level, content_in=None, **kwargs):
        if level is not None:
            _tag = 'h{0}'.format(level)
        super(H, self).__init__(content_in, **kwargs)


class Br(SelfClosingTag):
    _tag = 'br'
    _attributes = {}


class A(OneLineTag):
    _tag = 'a'
    _attributes = {}

    def __init__(self, link, content_in=None, **kwargs):
        kwargs['href'] = link
        super(A, self).__init__(content_in, **kwargs)


class Meta(SelfClosingTag):
    _tag = 'meta'
    _attributes = {}


class Ul(Element):
    _tag = 'ul'
    _attributes = {}


class Li(Element):
    _tag = 'li'
    _attributes = {}

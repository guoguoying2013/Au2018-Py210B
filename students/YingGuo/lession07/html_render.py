#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element():
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = [] if content is None else [content]
        self.kwargs = kwargs 


    def append(self, new_content):
        self.content.append(new_content)
             
    #what does ind mean in the test_html? why it is needed?
    def render(self, out_file, cur_ind=""):
        if cur_ind:
            out_file.write(cur_ind)

        for content in self.content:
            if self.kwargs is not None:
                open_tag = ["<{}".format(self.tag_name)]
                for x in self.kwargs:
                    open_tag.append(x)
                    open_tag.append("=")
                    open_tag.append('"{}"'.format(self.kwargs[x]))
                    open_tag.append(" ")
                open_tag.append(">\n")
                out_file.write("".join(open_tag))
            else:
                pass

            if cur_ind:
                out_file.write(cur_ind)

            try:
                content.render(out_file, cur_ind+self.indent)
            except AttributeError:
                out_file.write(self.indent)
                out_file.write(content)
                out_file.write("\n")
            
            if cur_ind:
                out_file.write(cur_ind)

            out_file.write("</{}>\n".format(self.tag_name))


#a subclass of Element with tag body
class Body(Element):
    tag_name = "body"

#subclass for paragraph
class P(Element):
    tag_name = "p"

class Html(Element):
    tag_name = "html"

class Title(Element):
    tag_name = "title"
    def render(self, out_file):
        for content in self.content:
            out_file.write("<{}>".format(self.tag_name))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag_name))

class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
            out_file.write("<{}>".format(self.tag_name))
            out_file.write(self.content[0])
            out_file.write("</{}>\n".format(self.tag_name))
            
    #change the test file with import pytest
    def append(self, content):
        raise NotImplementedError

class SelfClosingTag(Element):
    #somethinkg like <hr width="400" />
    def render(self, out_file, cur_ind=""):
        open_tag = ["<{} ".format(self.tag_name)]
        if self.kwargs:
            for x in self.kwargs:
                open_tag.append(x)
                open_tag.append("=")
                open_tag.append('"{}"'.format(self.kwargs[x]))
                out_file.write("".join(open_tag))
                out_file.write(" ")
        else:
            out_file.write("".join(open_tag))

        out_file.write("/>\n")
    

class Hr(SelfClosingTag):
    tag_name = "hr"

class Br(SelfClosingTag):
    tag_name = "br"

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
    
    def __init__(self, content = None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

class A(SelfClosingTag):
    tag_name = "a"

    def __init__(self,link,content, **kwargs):
        super().__init__(content, **kwargs)

class Header(SelfClosingTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag_name = level

    def render(self, out_file, cur_ind=""):
        for content in self.content:
            out_file.write("<{}>".format(self.tag_name))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag_name))

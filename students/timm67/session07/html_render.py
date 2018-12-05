#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    object.content = []

    def __init__(self, content=None):
        if content is not None:
            self.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        try:
            # TODO: may want to append to already opened file (i.e. call render multiple times)
            with open(out_file, 'w') as fd:
                for line in self.content:
                    try:
                        fd.write(line)
                    except IOError:
                        print("I/O Error with file [{0}] on writeline".format(out_file))
                        return
        except IOError:
            print("I/O Error with file [{0}] on open".format(out_file))
            return

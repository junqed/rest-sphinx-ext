# -*- coding: utf-8 -*-

"""
Allows collecting information from view functions (or methods)
with two special tags:
    
    # restmethod
    # restclass
"""


__author__ = "Eugene Fominykh"
__email__ = "junqed@gmail.com"

from sphinx.ext.autodoc import MethodDocumenter, ClassDocumenter


class RestfulViewDocumenter(MethodDocumenter):
    objtype = 'restmethod'
    titles_allowed = True
    content_indent = ''

    def add_directive_header(self, sig):
        pass


class RestfulClassViewDocumenter(ClassDocumenter):
    objtype = 'restclass'
    titles_allowed = True
    content_indent = ''

    def add_directive_header(self, sig):
        pass


def setup(app):
    app.add_autodocumenter(RestfulViewDocumenter)
    app.add_autodocumenter(RestfulClassViewDocumenter)

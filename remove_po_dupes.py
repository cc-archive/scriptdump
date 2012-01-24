# pofile template syntax converter
# 
# Written in 2011 by Christopher Allan Webber, Creative Commons
# 
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any
# warranty.
# 
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

# Convert pofiles from ${foo} style string substitutions to %(foo)s
# style for the great Jinja2 {% trans %} block conversion ;)

import copy
import sys
from cc.i18n.tools.support import polib_wrapped_write_po

from babel.messages.catalog import Catalog
from babel.messages.pofile import read_po

def convert_pofile(filename):
    pofile = read_po(file(filename, 'r'))

    new_catalog = Catalog(
        header_comment="", 
        locale=pofile.locale, 
        domain=pofile.domain)

    for msg in pofile:
        new_catalog[msg.id] = msg

    polib_wrapped_write_po(filename, new_catalog)

def main():
    filenames = sys.argv[1:]

    for filename in filenames:
        convert_pofile(filename)

if __name__ == '__main__':
    main()

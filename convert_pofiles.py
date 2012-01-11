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

import re
import sys
from babel.messages.pofile import read_po
from cc.i18n.tools.support import polib_wrapped_write_po


def convert_pofile(filename):
    podata = file(filename, 'r').read()
    converted = re.sub(
        "\$\{?(.+?)\}", lambda x: "%(" + x.groups()[0] + ")s", podata)
    file(filename, 'w').write(converted)
    pofile = read_po(file(filename, 'r'))
    for msg in pofile:
        msg.context = None

    polib_wrapped_write_po(filename, pofile)

def main():
    filenames = sys.argv[1:]

    for filename in filenames:
        convert_pofile(filename)

if __name__ == '__main__':
    main()

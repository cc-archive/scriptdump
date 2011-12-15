import os
import re
import sys

from rdflib import Literal

from cc.licenserdf.tools.support import load_graph, save_graph
from cc.i18n.gettext_i18n import ugettext_for_locale


TRANSLATION_BIT_RE = re.compile('\$\{([^\}]+)\}')


def convert_file(filename):
    gettext = ugettext_for_locale('en')
    graph = load_graph(os.path.abspath(filename))
    for subject, predicate, obj in graph.triples((
            None, None, None)):
        if hasattr(obj, 'language') and obj.language == 'i18n':
            graph.remove((subject, predicate, obj))
            new_obj = Literal(
                TRANSLATION_BIT_RE.sub(
                    lambda x: '${' + gettext(x.groups()[0]) + '}',
                    str(obj)),
                lang='i18n')
            graph.add((subject, predicate, new_obj))

    save_graph(graph, os.path.abspath(filename))


def main():
    filenames = sys.argv[1:]

    for filename in filenames:
        convert_file(filename)

if __name__ == '__main__':
    main()

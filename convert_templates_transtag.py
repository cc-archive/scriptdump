import re
import sys
from cc.i18n import gettext_i18n


gettext = gettext_i18n.ugettext_for_locale('en')

def countspace(some_str):
    """Count leading whitespace"""
    counter = 0
    for char in some_str:
        if char == " ":
            counter += 1
        else:
            break

    return counter


def nicer_args(args):
    arglines = args.strip().splitlines()
    if len(arglines) <= 1:
        return args

    newlines = [arglines[0]]
    for line in arglines:
        numspaces = countspace(line)
        if numspaces > 2:
            # skip two spaces
            newlines.append(line[2:])

    return '\n'.join(newlines)


def generate_trans_block(match):
    logical_msg = match.groups()[0]
    # args = [arg.strip().strip(',') for arg in match.groups()[1].strip().split(',')]
    args = match.groups()[1].strip()
    english_msg = gettext(logical_msg)
    if args:
        #return "{% trans " + ", ".join(args) + " %}" + english_msg + "{% endtrans %}"
        return "{% trans " + nicer_args(args) + " %}" + english_msg + "{% endtrans %}"
    else:
        return "{% trans %}" + english_msg + "{% endtrans %}"

def transform_template(template_text):
    regex = re.compile(
        r'{{ cctrans\(locale, [\'"]?(.+?)[\'"],?(.*?)\)\|safe ?}}',
        re.S)
    return regex.sub(generate_trans_block, template_text)

def main():
    filenames = sys.argv[1:]

    for filename in filenames:
        template_text = open(filename).read()
        transformed_template = transform_template(template_text)
        open(filename, 'w').write(transformed_template)

if __name__ == '__main__':
    main()

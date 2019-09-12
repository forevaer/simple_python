#!/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/bin/python3.7
"""

Usage:
    learn_docopt -n <name>
    learn_docopt -p <password>
    learn_docopt [-n <name>] [-p <pass>]
    learn_docopt

Options:
    -n=<name> username [default:yes]
    -p=<pass>  password [default:pass]
"""

from docopt import docopt

args = docopt(__doc__)
for key, value in args.items():
    print("{_key} = {_value}".format(_key=key, _value=value))

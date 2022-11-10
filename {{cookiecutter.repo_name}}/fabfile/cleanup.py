from __future__ import print_function

# stdlib
import os

# pypi
from fabric import task

# ==============================================================================


def pyc_clean(dir):
    findcmd = 'find %s -name "*.pyc" -print' % dir
    count = 0
    for f in os.popen(findcmd).readlines():
        count += 1
        print(str(f[:-1]))
        os.remove(str(f[:-1]))
    print("Removed %d .pyc files" % count)


def pyo_clean(dir):
    findcmd = 'find %s -name "*.pyo" -print' % dir
    count = 0
    for f in os.popen(findcmd).readlines():
        count += 1
        print(str(f[:-1]))
        os.remove(str(f[:-1]))
    print("Removed %d .pyo files" % count)


def makopy_clean(dir):
    """
    the mako templating language will compile `.mako` files
    into a `.mako.py` python package
    """
    findcmd = 'find %s -name "*.mako.py" -print' % dir
    count = 0
    for f in os.popen(findcmd).readlines():
        count += 1
        print(str(f[:-1]))
        os.remove(str(f[:-1]))
    print("Removed %d .mako.py files" % count)


@task
def cleanup_project(c):
    """
    cleans up several known types of cache/compiled files
    """
    print("cleaning up directory...")
    pyc_clean(".")
    pyo_clean(".")
    makopy_clean(".")

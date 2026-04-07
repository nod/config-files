#!/usr/bin/env python3
# shameless port of https://github.com/aniero/dotfiles/blob/master/install.rb

from glob import glob
from os import environ, getcwd, symlink, makedirs
from os.path import exists, expanduser, join, normpath
from platform import system
from sys import stderr

home = expanduser(environ['HOME'])

def install_sym(src, target):
    if exists(target):
        print("skipping {}, already exists".format(target))
    else:
        print("installing {} to {}".format(src, target))
        symlink(src, target)


def mkpath(p):
    return normpath(join(home, p))


def mksym(f, rmprefix='', dot=True):
    t = f.removeprefix(rmprefix)
    target = normpath(join(home, f'{"." if dot else ""}{t}'))
    src = normpath(join(getcwd(), f))
    install_sym(src, target)

# first, ensure `$HOME/.config` exists
# future me - i'm not symlinking this because it often exists on linux systems
# already and I don't want to try to reconcile the contents.  So just create
# the dir, then symlink the config-files/ repo contents into it
config_dir = mkpath(".config")
if not exists(config_dir):
    makedirs(config_dir)


# now do our toplevel dotfiles
for f in glob('dotfiles/*'):
    if any((f.startswith(x) for x in ('nope', 'README', 'install', 'tags', 'archive'))):
        continue
    mksym(f, rmprefix="dotfiles/", dot=True)



for f in glob('dotfiles/config/*'):
    if any((f.startswith(x) for x in ('nope', 'README', 'install', 'tags', 'archive'))):
        continue
    mksym(f, rmprefix="dotfiles/", dot=True)



for d in ('~/tmp', '~/.pyvs'):
    d_ = expanduser(d)
    if not exists(d_):
        print("making directory:", d_)
        makedirs(d_)
    else:
        print("skipping", d_, "already exists.")


# symlink ~/.secrets/ssh
if exists(normpath(join(home, ".secrets"))):
    ssh_dir =  normpath(join(home, '.ssh'))
    src = normpath(join(home, ".secrets/ssh"))
    install_sym(src, ssh_dir)
else:
    print("no .secrets, not linking .ssh")



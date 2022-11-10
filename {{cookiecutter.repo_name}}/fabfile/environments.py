from __future__ import print_function

# stdlib

# pypi
from fabric import task

# local
from . import constants
from .packages import python_packages

# ==============================================================================


@task
def env_install_python_packages(c):
    """
    installs the python packages into the virtualenv

    :param c: A `fabric.connection.Connection` instance.
              automatically dispatched by `@task`.
    """
    print("installing core packages...")
    for pkg_name, pkg_info in python_packages.items():
        if pkg_info.install:
            with c.cd("python-packages/%s" % pkg_name):
                print("\t", pkg_name)
                # c.run("pip --version", replace_env=False)
                c.run("pip install -e .", replace_env=False)


@task
def env_set_environment(c):
    """
    updates the `{{cookiecutter.repo_name}}_core` settings used by all applications;
    changes js/css dist directory

    :param c: A `fabric.connection.Connection` instance.
              automatically dispatched by `@task`.
    """
    if constants.environment not in ("production", "staging", "development"):
        raise ValueError("invalid `environment`")
    _root = constants.get_root(c)
    with c.cd(
        "%s/%s/src/{{cookiecutter.repo_name}}_pyramid/static/" % (_root, constants.LOCALPATH_pyramid)
    ):
        c.run("rm -rf ./-dist")
        if constants.environment == "development":
            c.run("mkdir -p ./-dist-development")
            c.run("ln -s ./-dist-development ./-dist")
        else:  # production/staging
            c.run("mkdir -p ./-dist-production")
            c.run("ln -s ./-dist-production ./-dist")

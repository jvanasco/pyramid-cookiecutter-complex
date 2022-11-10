from __future__ import print_function

# pypi
from fabric import task

# local
from .packages import python_packages

# ==============================================================================


@task
def _code_quality_runner(c, command):
    """
    runs `:param: command` on all first-party packages
    """
    if command not in ("black", "flake8"):
        raise ValueError("only `black` and `flake8` are supported")
    print("applying `%s` to packages: /python-packages/ ..." % command)
    fails = []
    for pkg_name, pkg_info in python_packages.items():
        if pkg_info.run_unit_tests:
            with c.cd("python-packages/%s" % pkg_name):
                print("\t", pkg_name)
                try:
                    c.run("%s ." % command, replace_env=False)
                except Exception as exc:
                    fails.append((pkg_name, exc))
                    print("*" * 40)
                    print("%s ERROR" % command.upper())
                    print(type(exc))
                    print(exc)
    if fails:
        print("Exceptions Encountered. See above for details.")
        print("Affected packages:")
        for pkg_name, exc in fails:
            print("\t", pkg_name)
    else:
        print("No fatal exceptions detected when running `%s`." % command)


@task
def code_quality_black(c):
    """
    runs `black` on all first-party packages
    """
    _code_quality_runner(c, "black")


@task
def code_quality_flake8(c):
    """
    runs `flake8` on all first-party packages
    """
    _code_quality_runner(c, "flake8")

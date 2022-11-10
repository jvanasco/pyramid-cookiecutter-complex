from __future__ import print_function

# stdlib
import os

# ==============================================================================

environment = os.environ.get("{{cookiecutter.env_base}}_ENVIRONMENT")
if environment not in ("production", "development", "staging"):
    raise ValueError(
        "must set {{cookiecutter.env_base}}_ENVIRONMENT to `production` or `development` or `staging`"
    )

LOCALPATH_pyramid = "python-packages/{{cookiecutter.repo_name}}_pyramid"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_root(c):
    """
    :param c: A `fabric.connection.Connection` instance.
              automatically dispatched by `@task`.
    """
    import {{cookiecutter.repo_name}}_core
    if environment == "production":
        return {{cookiecutter.repo_name}}_core.constants.FILESYSTEM_ROOTS["production"]
    elif environment == "development":
        return {{cookiecutter.repo_name}}_core.constants.FILESYSTEM_ROOTS["development"]
    elif environment == "staging":
        return {{cookiecutter.repo_name}}_core.constants.FILESYSTEM_ROOTS["staging"]
    raise ValueError("invalid `environment`")


def get_pyramid_config_ini(c):
    """
    :param c: A `fabric.connection.Connection` instance.
              automatically dispatched by `@task`.
    """
    _root = get_root(c)
    if environment == "production":
        path = os.path.join(_root, LOCALPATH_pyramid)
        file = os.path.join(path, "production.ini")
        return file
    elif environment == "development":
        path = os.path.join(_root, LOCALPATH_pyramid)
        file = os.path.join(path, "development.ini")
        return file
    raise ValueError("invalid `environment`")

# stdlib
import os

# ==============================================================================


# set up the env
ENVIRONMENT = os.environ.get("{{cookiecutter.env_base}}_ENVIRONMENT")
FILESYSTEM_ROOTS = {
    "production": "/var/www/sites/{{cookiecutter.project_directory}}-production",
    "staging": "/var/www/sites/{{cookiecutter.project_directory}}-staging",
    "development": "/Volumes/Development/webserver/sites/{{cookiecutter.project_directory}}",
}
if ENVIRONMENT in FILESYSTEM_ROOTS:
    FILESYSTEM_DIR_FLAGS = "%s/config/flags" % FILESYSTEM_ROOTS[ENVIRONMENT]
else:
    raise ValueError("invalid environment: %s" % ENVIRONMENT)
if not os.path.exists(FILESYSTEM_DIR_FLAGS):
    raise ValueError("invalid flags directory `%s`" % FILESYSTEM_DIR_FLAGS)
    exit()

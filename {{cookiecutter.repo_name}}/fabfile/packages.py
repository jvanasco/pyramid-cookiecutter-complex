from collections import namedtuple


# ==============================================================================


PackageTuple = namedtuple("PackageTuple", "install,is_daemon,run_unit_tests")

PostInstallTuple = namedtuple("PostInstallTuple", "install,is_daemon,run_unit_tests")


# ------------------------------------------------------------------------------

# these MUST be in the `python-packages` directory
# keys are filepaths
python_packages = {
    "{{cookiecutter.repo_name}}_core": PackageTuple(install=True, is_daemon=False, run_unit_tests=True),
    "{{cookiecutter.repo_name}}_model": PackageTuple(install=True, is_daemon=True, run_unit_tests=True),
    "{{cookiecutter.repo_name}}_pyramid": PackageTuple(
        install=True, is_daemon=True, run_unit_tests=True
    ),
}

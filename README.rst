============================
pyramid-cookiecutter-complex
============================

A cookiecutter (project template) for organizing a complex Pyramid project.

This project is designed to be used in addition to the official Pyramid
cookiecutters, as it does not generate the scaffolding for a Pyramid project
itself, but instead generates the scaffolding to contain a complex Pyramid
project.

This cookiecutter is NOT designed for simple Pyramid projects, but to aid those
developers who are building complex projects that may span several Pyramid
applications, Twisted services, and commandline tools.

What is a complex project?

This cookiecutter creates a project with the following features:

* The scaffold creates a structure to manage a Pyramid application as three
  separate packages under the `python-packages` namespace.
  * `project_core` - shared library functions
  * `project_model` - model; e.g. sqlalchemy definition
  * `project_pyramid` - the pyramid application; e.g. the output of an official pyramid cookiecutter
  This faceting is designed to help users develop towards large integrated
  projects.
* Support for running in multiple environments:
    * development
    * staging
    * production
* Managing the project and deployment through (Fabric)[https://fabfile.org]. Some default commands are provided.
* Maintaining assets and server configurations in git
* Maintaining SQL triggers, views, etc

This cookiecutter was created based on development patterns used in production
for many years.


Requirements
------------

*   Python 3.6+
*   `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_


Usage
-----

#.  Generate a "Complex" project

    .. code-block:: bash

        $ cookiecutter gh:jvanasco/pyramid-cookiecutter-complex
        
#.  Install it:


    .. code-block:: bash

        $ cd {{project_directory}}
        $ open docs/INSTALL.txt
        
    Follow the directions.        

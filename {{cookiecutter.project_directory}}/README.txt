This project is a scaffold/cookiecutter for generating more complex Pyramid 
projects. 

The template/repo is licensed under the MIT license.

It is recommended to maintain this file as your project grows.

It is also recommended to utilize an encryption system like
[Blackbox](https://github.com/StackExchange/blackbox), which would create a
toplevel `/keyrings` directory to manage secret files.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

IMPORTANT:

This project REQUIRES the following environment variables to be set:

* `{{cookiecutter.env_base}}_ENVIRONMENT`
  This is read by `{{cookiecutter.repo_name}}_core/constants.py`, which is
  invoked by the Fabric management tool and most Python packages.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

* `/assets`
  * This directory should be used for organizing project assets, such as PSDs.
    As your project evolves, please consider splitting this out into another
    directory.

* `/config`
  * This directory is intended to hold server and service configuration files

* `/docs`
  * This directory should be used for organizing project documentation.
    Initially this will contain installation instructions.
    
* `/fabfile`
  * This system utilizes [Fabric](https://fabfile.org/) for installation,
    configuration and deployment.
    
    Type `fab -l` on the top directory structure to see a listing of the default
    routines. These should be grown and edited with your project!

* `/python-packages`
  * This layout splits a Pyramid application into 3 components:
    * `{project}_pyramid` The pyramid app, as if using a normal cookiecutter 
    * `{project}_core` package for shared library functions
    * `{project}_model` package for sqlalchemy model
    This design is utilized because, as a project grows it often requires
    additional libraries or projects.  For example, you may want to build a
    small commandline tool, a Twisted service, or a series of other packages.
    Instead of doing everything within Pyramid and then splitting things out,
    we are trying to separate all these things from the start.

* `/tools`
  * This directory should be used for holding commandline tools.  If they are
    written in Python, it is STRONGLY recommended to only write simple scripts
    that leverage the necessary libraries in `/python-packages/`.  It often
    makes sense to maintain a new python module as
    `/python-packages/{project}_tools` and have these scripts reference that.

* `/www`
  * This directory should be used for holding static websites to be served
    by nginx, such as maintenance/downtime versions of your project, or
    ancillary microsites.



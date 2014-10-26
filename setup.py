#!/usr/bin/env python

from setuptools import setup, find_packages

RPM_REQUIRED_DEPS = "python-flask"
 
## HACK FOR DEPS IN RPMS
from setuptools.command.bdist_rpm import bdist_rpm
def custom_make_spec_file(self):
    spec = self._original_make_spec_file()
    line= "%description"
    spec.insert(spec.index(line) - 1, "requires: %s" % RPM_REQUIRED_DEPS)
    line= "%install"
    spec.insert(spec.index(line) + 2, "install -D -m 700 ../../../../../extra/githubhooks.init  %{buildroot}%{_initrddir}/githubhooks")
    line= "%files -f INSTALLED_FILES"
    spec.insert(spec.index(line) + 2, "%{_initrddir}/githubhooks")
    spec.append("%post")
    spec.append("/sbin/chkconfig --add githubhooks")
    spec.append("%preun")
    spec.append("if [ $1 -eq 0 ] ; then")
    spec.append("    /sbin/service githubhooks stop >/dev/null 2>&1")
    spec.append("    /sbin/chkconfig --del githubhooks")
    spec.append("fi")
    return spec
bdist_rpm._original_make_spec_file = bdist_rpm._make_spec_file
bdist_rpm._make_spec_file = custom_make_spec_file
## END OF HACK

setup(
    name = "githubhooks",
    version = "0.1",
    packages = find_packages(),
    entry_points = {
        'console_scripts': ['githubhooks=githubhooks.server:server'],
    },
    install_requires = [
        "Flask"
    ],
)

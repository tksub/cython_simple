from distutils.command.build import build
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""
    def run(self):

        # Import numpy here, only when headers are needed
        import numpy

        # Add numpy headers to include_dirs
        self.include_dirs.append(numpy.get_include())

        # Call original build_ext command
        build_ext.run(self)

ext_modules = [Extension("function_calc_distance_cython", ["function_calc_distance_cython.pyx"])]

setup(
    name = 'cython test',
    cmdclass = {'build_ext': CustomBuildExtCommand}, 
    install_requires = ['numpy'],
    ext_modules = ext_modules
)
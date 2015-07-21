import warnings

try:
    from Cython.Distutils import build_ext
    from setuptools import setup, Extension
    HAVE_CYTHON = True
except ImportError as e:
    warnings.warn(e.message)
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext

_hdbscan_tree = Extension('hdbscan/_hdbscan_tree',
                          sources=['hdbscan/_hdbscan_tree.pyx'])
_hdbscan_linkage = Extension('hdbscan/_hdbscan_linkage',
                             sources=['hdbscan/_hdbscan_linkage.pyx'])

def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()

configuration = {
    'name' : 'hdbscan',
    'version' : '0.1',
    'description' : 'Clustering based on density with variable density clusters',
    'long_description' : readme(),
    'classifiers' : [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    'keywords' : 'cluster clustering density hierarchical',
    'url' : 'http://github.com/lmcinnes/hdbscan',
    'maintainer' : 'Leland McInnes',
    'maintainer_email' : 'leland.mcinnes@gmail.com',
    'license' : 'BSD',
    'packages' : ['hdbscan'],
    'install_requires' : ['sklearn>=0.16',
                          'cython >= 0.17'],
    'ext_modules' : [_hdbscan_tree, _hdbscan_linkage],
    'cmdclass' : {'build_ext' : build_ext}
    }

if not HAVE_CYTHON:
    _hdbscan_tree.sources[0] = '_hdbscan_tree.c'
    _hdbscan_linkage.sources[0] = '_hdbscan_linkage.c'
    configuration['install_requires'] = ['sklearn>=0.16']

setup(**configuration)
 
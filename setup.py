from setuptools import setup



setup(
    name = 'target-encoder',
    version = '0.0.1',
    description = 'An custom mdoule for GLM Regressor.',
    py_modules = ["Target_Encoder"],
    package_dir = {'':'src'},
#     package = ['Target_Encoder'],
#     author = 'Jinhang Jiang, Karthik Srinivasan',
#     author_email = 'jinhang@asu.edu',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/SKalahast/target-encoder',
    include_package_data=True,
    
    
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    install_requires = [
        'pandas ~= 1.4.2',
        'numpy ~= 1.21.5'
    ],
    
    keywords = ['Data Science'],
    
)

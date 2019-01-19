from setuptools import setup, find_packages

setup(
    name             = 'jaram_rhythmgamewiki_2019',
    version          = '0.2',
    description      = 'CLI rhythmgamewiki in jaram, 2019 (winter workshop)',
    author           = 'Min Woo Son',
    author_email     = 'mwson987@gmail.com',
    url              = 'https://github.com/Jaram2019/minwoo',
    download_url     = 'https://github.com/Jaram2019/minwoo',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['jaram', 'wiki'],
    python_requires  = '>=3',
    package_data     =  {},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)

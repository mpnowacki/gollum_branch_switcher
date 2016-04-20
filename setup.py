from setuptools import setup

setup(
    name='gollum_branch_switcher',
    version='0.0.1',
    author='Michał Nowacki',
    author_email='michal@nowacki.eu.com',
    description='branch switcher for gollum',
    license="MIT/X",
    packages=['gollum_branch_switcher'],
    entry_points={'console_scripts': ['gbs = gollum_branch_switcher:print']},
    install_requires=[
        'Flask==0.10.1',
        'GitPython==1.0.1',
    ],
)
1
1

from distutils.core import setup


with open('requirements.txt') as f:
      content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='snowflakes_magic',
      version='1.0',
      description='Jupyter Connector to Snowflake',
      author='Gildas Darex TOSSA',
      author_email='gtossa@lafourchette.com',
      url='none',
      install_requires=requirements,
      packages=['snowflakes']

     )


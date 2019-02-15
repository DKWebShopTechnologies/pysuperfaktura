from distutils.core import setup

setup(
    name='pysuperfaktura',
    version='0.6b',
    packages=['pysuperfaktura'],
    url='https://github.com/EndevelCZ/pysuperfaktura',
    license='BSD',
    author='backslash7',
    author_email='lukas.stana@it-admin.sk',
    description='Python API for superfaktura.sk', requires=['requests']
)

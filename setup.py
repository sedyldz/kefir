from setuptools import setup, find_packages
import re

with open("README.md") as f:
    readme = f.read()

TAG_RE = re.compile(r'<[^>]+>')

readme_clean = TAG_RE.sub('', readme)

setup(
    name='kefir',
    version='0.1.0',
    description='Kefir is a natural language processing kit for Turkic languages',
    long_description=readme_clean,
    url='https://github.com/yogurt-cultures/kefir',
    author='Yogurt Cultures',
    author_email='cediddi@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Turkish',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
    ],
)

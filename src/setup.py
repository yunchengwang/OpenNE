from setuptools import setup, find_packages

setup(
    name="grll",
    url="https://github.com/yunchengwang/OpenNE",
    license="MIT",
    author="USCMCL",
    description="Forked from THUNLP OpenNE",
    packages=find_packages('grll'),
    long_description=open("../README.md").read(),
    zip_safe=False,
    setup_requires=[
        'numpy==1.14',
        'networkx==2.0',
        'scipy==0.19.1',
        'tensorflow>=1.12.1',
        'gensim==3.0.1',
        'scikit-learn==0.19.0'
    ]
)
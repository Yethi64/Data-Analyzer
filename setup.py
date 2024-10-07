from setuptools import setup

setup(
    name='absoprtion_data-analyzer',
    version='0.1',
    install_requires=[
        'streamlit',
        'numpy',
        'pandas',
        'matplotlib==3.6.3',
        'scipy',
        'wheel',
    ],
    python_requires='>=3.7'
)

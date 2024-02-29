from setuptools import setup, find_packages

setup(
    name='TradingC',
    version='0.0.1',
    packages=find_packages(),
    install_requires=["TradingB <= 0.0.1"],
    description='Trade in Binance when perpetual price is higher than actual stock price',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='gamingGGa',
    author_email='admin@example.com',
    url='https://github.com/GamingGGa/TradingC',
    project_urls={
        'Source': 'https://github.com/GamingGGa/TradingC'
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
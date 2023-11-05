from setuptools import setup, find_packages

setup(
    name='ArtisticAI',
    version='0.1.0',
    author='ChrisPeterson',
    author_email='chrapeterson@gmail.com',
    description='AI-powered tool for assisting artists and designers with creative prompts and design suggestions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/scapecap/ArtisticAI',
    project_urls={
        'Bug Tracker': 'https://github.com/scapecap/ArtisticAI/issues',
        'Documentation': 'https://github.com/scapecap/ArtisticAI/wiki',
        'Source Code': 'https://github.com/scapecap/ArtisticAI',
    },
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        # Add project dependencies here
        # 'numpy',
        # 'pandas',
        # 'tensorflow',
        # etc.
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='art design ai creativity',
    entry_points={
        'console_scripts': [
            'artisticai=ArtisticAI.cli:main',
        ],
    },
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)

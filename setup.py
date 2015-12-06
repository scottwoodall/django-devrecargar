import setuptools

setuptools.setup(
    name="devrecargar",
    version="0.1.4",
    url="https://github.com/scottwoodall/django-devrecargar",
    author="Scott Woodall",
    author_email="scott.woodall@gmail.com",

    description="""
        A Django app that automatically reloads your browser when a file
        (py, html, js, css) changes.
    """,

    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=['watchdog'],
    include_package_data=True,

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)

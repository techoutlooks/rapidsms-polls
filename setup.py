from setuptools import setup, find_packages

setup(
    name='rapidsms-polls',
    version='0.1',
    license="BSD",

    required_packages = [line.strip('\n') for line in
                     open('requirements.txt').readlines()],

    dependency_links = [
        "-e git+https://github.com/techoutlooks/rapidsms.git@develop#egg=rapidsms",
        "-e git://github.com/mvpdev/django-eav.git@d41f10468c428e036725b48518ecd846e7580c9d#egg=django_eav-master"
    ],

    description='An application for a simple communication modality with SMS users: prompted questions, simple, training-less answers.',
    long_description=open('README.rst').read(),
    author='David McCann',
    author_email='david.a.mccann@gmail.com',

    url='http://github.com/daveycrockett/rapidsms-polls',
    download_url='http://github.com/daveycrockett/rapidsms-polls/downloads',

    include_package_data=True,

    packages=find_packages(),
    package_data={'poll':[
        'templates/*/*.html',
        'templates/*/*/*.html',
        'static/images/*',
        'static/javascripts/*',
        'static/stylesheets/*',
        'static/icons/silk/*']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

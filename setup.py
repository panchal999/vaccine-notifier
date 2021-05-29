from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    url = "",
    author="Parth Panchal",
    author_email="parthnp98@gmail.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    name='vaccine-notifier',
    version='0.0.1',
    description='Notify vaccination availability - Play Music/Song and Send Desktop Notifaction for vaccine availability',
    py_modules=["trigger"],
    package_dir={'': 'src'},
    install_requires = [
       "requests>=2.25.1",
       "pydub>=0.3.3",
       "notify-py>=0.3.3"
    ]
)
# World of Medicine
#### Desktop application
An application for automating and maintaining medical document management.
At the moment, 2 automated workstations have been implemented:
1) A rehabilitologist in the conditions of the department of medical rehabilitation
2) A botulinum therapy room

you need to set the workplace settings (medical organization data, lists of doctors, ward numbers, etc.) in the files ('dep_omr.py' or 'dep_bta.py', respectively, by opening them using notepad) along the path 'wom/settings/'

NB! The application uses 'poetry', [installation instructions](https://python-poetry.org/docs/#installation)

### Installation
```ch
make install
```
or
```ch
poetry install
```
### Usage
```ch
make start
```
or
```ch
poetry run app
```

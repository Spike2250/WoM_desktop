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

### ScreenShots
![main_menu](https://i.postimg.cc/nr6q99G3/2024-05-16-15-20-34.png)
![omr_main_menu](https://i.postimg.cc/0QXYxBMR/2024-05-16-15-21-41.png)
![omr_patient_card](https://i.postimg.cc/L8kjhXYV/2024-05-16-15-22-45.png)
![omr_icf](https://i.postimg.cc/kXbQ3w7z/2024-05-16-15-23-46.png)
![bta_protocol](https://i.postimg.cc/9fVtBT5S/2024-05-16-15-25-01.png)
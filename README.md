# GIT download count generator
This is simple shell script to save the download count of a GitHub repository to a .xlsx file.

## Prerequisits

* Install the xlsxwriter python package (for writing Excel sheets)

```
    python3 -m pip install xlsxwriter
```

## How to use

* Clone the project
```
    git clone https://github.com/dakshika/git-download-count-generator.git
```
* Run 

```
python3 git-download-status.py
```

* Enter user name and repo name. Example:

```
Enter User name: sys-bio
Enter Project name: tellurium
```

> Check the exported file on export folder

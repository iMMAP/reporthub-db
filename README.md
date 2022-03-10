# Introduction
This project defines the data model of ReportHub and extracts current models from MongoDB


## Quick install

1) Install the latest version of python and virtualenv.
```
virtualenv installation:
https://virtualenv.pypa.io/en/latest/installation.html
```
2) Clone this repository
```
git clone git@github.com:iMMAP/reporthub-db.git
```
4) Create virtualenv environment
```
cd reporthub-db
virtualenv --python=<YOUR_LOCAL_PYTHON_PATH> .venv
```
3) Install packages
```
pip install -r requirements.txt
```
4) Activate your environment
```
source .venv/bin/activate
```


## Data Model

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```
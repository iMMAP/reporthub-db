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
report <|-- AveryLongClass : Cool
activity *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
report : size()
report : int chimp
report : int gorilla
Class08 <--> C2: Cool label
```

```mermaid
erDiagram
CAR ||--o{ NAMED-DRIVER : allows
CAR {
    string registrationNumber
    string make
    string model
}
PERSON ||--o{ NAMED-DRIVER : is
PERSON {
    string firstName
    string lastName
    int age
}
```
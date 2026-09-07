# Simple Pygames Examples 

This folder contains simple Pygame examples using _*pygame-ce*_. All of the examples use asynchio asynchronous methods so that they can be compiled using _*pygbag*_.

The current list of examples:

+ The simplest Example




## Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

## Activate the Virtual Environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## Install Dependencies

Once the virtual environment is active:

```bash
python -m pip install --upgrade pip
```

Install packages:

+ pygame-ce
+ pygbag

_*Do not install package pygame*_ it is original fork but is less supported.


Once the virtual environment is activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should be in the project's root directory:

```text
MyGame/
├── main.py
├── requirements.txt
├── Art/
│   └── ...
└── venv/
```

### Example `requirements.txt`

```text
pygame-ce
pygbag
```

### This Repo has following set up

'''text
'Simple Example'/
├── 'A game Folder'
│    └── main.py
     ├── requirements.txt (optional)
     ├── Art/
          └── ...
├── requirements.txt
└── .venv


'''

## Deactivate

When finished:

```bash
deactivate
```

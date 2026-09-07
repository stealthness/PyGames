# Simple Pygames Examples 

This folder contains simple Pygame examples using _*pygame-ce*_. All of the examples use asynchio asynchronous methods so that they can be compiled using _*pygbag*_.

The current list of examples:

+ The simplest Example




## Create a Virtual Environment

We recommend using a virtual environment to manage dependencies for your project. This ensures that the packages you 
install do not interfere with other projects or system-wide packages. We can check which python version is being used by running the following command:

```bash
python --version
```

Using following command which other python versions are installed in your system:

```bash
py -0
```
or
```
py --list
```

We would then see something like this:

```text
 -V:3.13 *        Python 3.13 (64-bit)
 -V:3.12          Python 3.12 (64-bit)
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

or using specified python version:

```bash
py -3.13 -m venv .venv
```

## Activate the Virtual Environment

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## Install Dependencies

Once the virtual environment is active:

```bash
python -m pip install --upgrade pip
```

Install packages:

+ pygame-ce
+ pygbag
+ _*Do not install package pygame*_ it is original fork but is less supported.

We can install from the command line using pip:

```bash
pip install pygame-ce pygbag
```

Or once the virtual environment is activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should be in the project's root directory:

```text
MyGame/
└── dev/
│   ├── main.py
│   ├── Art/
│   └── ...
├── requirements.txt
└── .venv/
```

Note 
+ that the `requirements.txt` file is optional. If you do not have one, you can install the packages directly using pip as shown above.
+ That `main.py` is in `dev` folder, but it can be in any folder this will be important later when we compile the game using pygbag.

An Example `requirements.txt`

```text
pygame-ce
pygbag
```

## Deactivate the Virtual Environment

When finished:

```bash
deactivate
```

## Compile the Game using pygbag

from comand line we create a archive of the game using pygbag:

```bash
python -m pygbag --archive dev\main.py
```

Notes
+ The `--archive` option creates a zip file of the game, which can be run in a web browser. This is also required by Itch.io to run web browser games
+ The `dev\main.py` is the path to the main script of the game. It must be called `main.py`.
+ On windows that `\` is used.

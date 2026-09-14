import os


def get_base_dir() -> str:
    """
    Return the base directory to use for loading assets.

    By default this returns the directory containing this file (the game's folder).
    If you want to change behavior for pygbag builds (where assets live at root),
    set the environment variable `PYGBAG_BASE` to `1` or change this function.
    This centralizes the location so switching between Windows and pygbag is easy.
    """
    # Allow override from environment for alternate build systems
    if os.environ.get("PYGBAG_BASE") == "1":
        return ""
    return os.path.dirname(__file__)


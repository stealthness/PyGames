import os


def get_base_dir(pygbag_build = False) -> str:
    """
    Return the base directory to use for loading assets.

    By default, we use the current working directory. Unless pygbag_build is set to True then cwd is ""
    """
    # Allow override from environment for alternate build systems
    if pygbag_build:
        return ""
    return os.path.dirname(__file__)


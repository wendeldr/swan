import os
from pathlib import Path


def relative_path_match_phase(match: str) -> str:
    module_path = os.path.abspath(os.path.join('..'))
    path = Path(module_path)

    # loop through path till match isn't found and return x
    x=''
    for x in range(len(path.parents)-1):
        if match not in path.parents[x-1]:
            break
    return x
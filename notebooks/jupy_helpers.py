import collections
import itertools

from IPython.core.magic import register_line_magic
from IPython.display import HTML, display


def set_background(color):
    script = (
        "var cell = this.closest('.jp-CodeCell, .cell');"
        "var editor = cell.querySelector('.jp-Editor, .input_area');"
        "editor.style.background='{}';"
        "this.parentNode.removeChild(this)"
    ).format(color)

    display(HTML('<img src onerror="{}">'.format(script)))


@register_line_magic
def background(color):
    set_background(color)


@register_line_magic
def exercise(_):
    set_background("Bisque")


@register_line_magic
def validate(_):
    set_background("Khaki")


@register_line_magic
def head(line):
    """Print first few lines from a file without using the `head` utility."""
    path, *args = line.split()
    if len(args) == 0:
        args = [5]
    
    with open(path) as infile:
        lines = itertools.islice(infile, *map(int, args))
        print("".join(lines))

@register_line_magic
def tail(line):
    """Print the last few lines from a file without using the `tail` utility."""
    path, *args = line.split()
    if len(args) == 0:
        args = [5]

    with open(path) as infile:
        lines = iter(collections.deque(infile, maxlen=int(args[0])))
        print("".join(lines))

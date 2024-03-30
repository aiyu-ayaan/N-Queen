from enum import Enum


class State(Enum):
    N_QUEEN = 'N-Queens Problem'


def print_board_in_markdown(size: int) -> str:
    markdown = ' ``` '
    markdown += '\n'
    for i in range(size + 1):
        for j in range(size):
            markdown += '#\t'
        markdown += '\n'
    markdown += ' ``` '
    return markdown

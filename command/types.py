import os

from DotIndex import DotIndex
from pathlib import Path
from typing import Callable

__all__ = [
    "_CommandManager",
    "_Command",
    "_Display"
]

class _CommandManager:
    def __init__(self): ...
    def add_command(self, command): ...
    def command(self, command: str) -> str: ...
    def _hook_display(self, display) -> None: ...

    commands: dict[str, '_Command']
    display: '_Display'
    previous_commands: list[str]

class _Command:
    def __init__(self, command_name: str, help_string: str, callback: Callable[..., str], container): ...
    def __str__(self) -> str: ...

    command_name: str
    help_string: str
    callback: Callable

class _Display:
    def __init__(self) -> None: ...
    def term_size(self) -> DotIndex: ...
    def display_text(self, text: str, disable_auto_wrap: bool=False, allow_printing: bool=True) -> list[str]: ...
    def keyboard_event(self, key: int) -> None: ...
    def _correct_cur_pos(self, string: list[str], ps1_length: int=0) -> str: ...
    def _insert_character(self, char: str) -> None: ...
    def _start(self, default_path: Path=Path(os.path.expanduser("~/"))) -> None: ...
    def _get_ps1(self) -> str: ...
    def _string_length(self, text: str) -> int: ...
    def _print(self, text: str) -> None: ...
    def _hook_manager(self, manager: _CommandManager) -> None: ...

    manager: '_CommandManager'
    path: Path
    current_input: str
    escape_sequence: list[int]
    cursor_position: int
    past_index: int
    previous_line: str

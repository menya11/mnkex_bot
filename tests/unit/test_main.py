from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable

    from harness import CommandResult

pytestmark = pytest.mark.unit


def test_main_prints_project_greeting(run_main: Callable[[], CommandResult]) -> None:
    # Locks: the console entry point prints the project greeting and nothing else.
    result = run_main()
    assert result.stdout == "Hello from mnkex-bot!\n"
    assert result.stderr == ""

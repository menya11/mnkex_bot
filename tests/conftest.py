from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from harness import invoke_main

if TYPE_CHECKING:
    from collections.abc import Callable

    from harness import CommandResult


@pytest.fixture
def run_main(capsys: pytest.CaptureFixture[str]) -> Callable[[], CommandResult]:
    def run() -> CommandResult:
        return invoke_main(capsys)

    return run

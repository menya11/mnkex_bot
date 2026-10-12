from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from mnkex_bot import main

if TYPE_CHECKING:
    import pytest


@dataclass(frozen=True, slots=True)
class CommandResult:
    stdout: str
    stderr: str


def invoke_main(capsys: pytest.CaptureFixture[str]) -> CommandResult:
    main()
    captured = capsys.readouterr()
    return CommandResult(stdout=captured.out, stderr=captured.err)

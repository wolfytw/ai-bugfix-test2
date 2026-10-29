import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from todo import TodoList, parse_date  # noqa: E402


def test_add_returns_display_number():
    todo = TodoList()
    assert todo.add("買牛奶") == 1
    assert todo.add("寫作業") == 2


def test_blank_title_is_rejected():
    with pytest.raises(ValueError):
        TodoList().add("   ")


def test_bad_due_date_is_rejected():
    with pytest.raises(ValueError):
        TodoList().add("報告", "明天")


def test_parse_date():
    assert parse_date("2026/9/5") == date(2026, 9, 5)


def test_render_shows_numbers_from_one():
    todo = TodoList()
    todo.add("繳報告", "2026/10/30")
    todo.add("運動")
    assert todo.render() == "1. [ ] 繳報告（2026/10/30）\n2. [ ] 運動"


def test_pending_lists_unfinished_tasks():
    todo = TodoList()
    todo.add("A")
    todo.add("B")
    todo.tasks[0].done = True
    assert [t.title for t in todo.pending()] == ["B"]

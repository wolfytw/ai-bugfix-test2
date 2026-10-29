"""小小待辦清單：「讓 AI 修一個 Bug」實作活動用的練習程式。

執行 `python todo.py` 可以看到範例輸出。
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    due: str | None = None  # 截止日，格式 "YYYY/M/D"，例如 "2026/9/5"
    done: bool = False


def parse_date(text: str) -> date:
    """把 "2026/9/5" 轉成 date。"""
    year, month, day = (int(part) for part in text.split("/"))
    return date(year, month, day)


class TodoList:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add(self, title: str, due: str | None = None) -> int:
        """新增任務，回傳畫面上顯示的編號（從 1 開始）。"""
        title = title.strip()
        if not title:
            raise ValueError("標題不能空白")
        if due is not None:
            parse_date(due)  # 格式不對會丟出 ValueError
        self.tasks.append(Task(title, due))
        return len(self.tasks)

    def complete(self, number: int) -> None:
        """把畫面上編號為 number 的任務標成完成。"""
        self.tasks[number].done = True

    def pending(self) -> list[Task]:
        return [t for t in self.tasks if not t.done]

    def sorted_by_due(self) -> list[Task]:
        """有截止日的任務，依截止日由近到遠排序。"""
        with_due = [t for t in self.tasks if t.due]
        return sorted(with_due, key=lambda t: t.due)

    def overdue(self, today: date) -> list[Task]:
        """回傳已經過期的任務。"""
        result = []
        for t in self.tasks:
            if t.due and parse_date(t.due) <= today:
                result.append(t)
        return result

    def summary(self) -> str:
        """例如「已完成 1/3（33%）」。"""
        done = sum(1 for t in self.tasks if t.done)
        total = len(self.tasks)
        percent = done * 100 // total
        return f"已完成 {done}/{total}（{percent}%）"

    def render(self) -> str:
        lines = []
        for i, t in enumerate(self.tasks, start=1):
            box = "x" if t.done else " "
            due = f"（{t.due}）" if t.due else ""
            lines.append(f"{i}. [{box}] {t.title}{due}")
        return "\n".join(lines)


if __name__ == "__main__":
    todo = TodoList()
    todo.add("繳期中報告", "2026/10/30")
    todo.add("讀 GitHub 文件", "2026/9/5")
    todo.add("報名說明會", "2026/11/2")
    todo.complete(1)
    print(todo.render())
    print(todo.summary())

# 🐞 讓 AI 修一個 Bug：15 分鐘實作

這個 repo 裡的待辦清單程式 `todo.py` 藏了幾個 bug，Issues 分頁已經開好對應的練習題（🟢 簡單、🟡 中等、🔴 挑戰）。
你的任務**不是自己修**，而是把問題寫清楚，交給 Copilot 修，再當它的審查者。

| 步驟 | 做什麼 | 時間 |
|---|---|---|
| 1 | 按右上角 **Use this template → Create a new repository**，建立自己的練習 repo（選 Public） | 1 分 |
| 2 | 到 **Issues** 挑一題，按 **Edit** 改寫描述：重現步驟、預期結果、實際結果、驗收條件（格式見下方） | 3 分 |
| 3 | 在 Issue 右側 **Assignees** 選 **Copilot**，等它開出 Pull Request | 4 分 |
| 4 | 打開 PR → **Files changed** 讀 diff，對照測試結果，至少留一則 review 意見 | 4 分 |
| 5 | 測試綠燈後按 **Merge**，回到 Issue 確認它已自動關閉 | 1 分 |

> 💡 Issues 分頁是空的？到 **Actions → 建立練習 Issue → Run workflow** 手動跑一次。
> 💡 PR 下方的檢查卡在「等待核准」？按 **Approve and run workflows** 讓測試開始跑。

## 好 Issue 的骨架（複製後填空）

```markdown
### 重現步驟
1. todo = TodoList()
2. ……
3. ……

### 預期結果
……

### 實際結果
……

### 驗收條件
- [ ] 輸入……時，結果應該是……
- [ ] 邊界情況（例如空清單）要……
- [ ] 新增對應的單元測試，且所有測試通過
```

## Review 時看這三件事

1. **改對地方了嗎？** diff 只改了跟 Issue 有關的程式嗎？
2. **測試真的證明修好了嗎？** 有沒有新增「修正前會失敗」的測試？驗收條件每一條都有測到嗎？
3. **還能更好嗎？** 命名、邊界情況、錯誤訊息，至少提出一點。

## 自己跑跑看

```bash
python todo.py      # 看範例輸出
pip install pytest
pytest -v           # 執行測試
```

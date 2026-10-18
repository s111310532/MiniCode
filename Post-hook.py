# 在 write 工具執行完畢處
def write(filepath: str, content: str) -> str:
    # ... 原本的寫入邏輯 ...
    save_file(filepath, content)
    
    # 自動反饋檢查結果
    lint_report = lint_file(filepath)
    return f"檔案已成功寫入。\n[語法診斷報告]\n{lint_report}"

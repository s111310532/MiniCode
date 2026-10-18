import subprocess
from pathlib import Path

def lint_file(filepath: str) -> str:
    """使用 ruff 檢查 Python 檔案是否有語法錯誤或風格問題。"""
    path = Path(filepath)
    if not path.exists():
        return f"Error: 找不到檔案 {filepath}"
    
    if path.suffix != ".py":
        return f"略過檢查：{filepath} 不是 Python 檔案。"

    result = subprocess.run(
        ["ruff", "check", str(path)],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return f"✓ {filepath} 語法檢查通過，無任何錯誤。"
    
    return f"⚠ {filepath} 檢查出以下問題，請修正：\n{result.stdout}"

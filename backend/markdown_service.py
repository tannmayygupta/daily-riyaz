from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


def save_entry(content: str):

    today = datetime.now()

    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")

    notes_dir = BASE_DIR / "notes" / year / month

    notes_dir.mkdir(parents=True, exist_ok=True)

    file_path = notes_dir / f"{day}.md"

    markdown_content = f"""# Riyaz Entry

Date: {today.strftime("%Y-%m-%d")}

## Learned Today

{content}
"""

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    return str(file_path)
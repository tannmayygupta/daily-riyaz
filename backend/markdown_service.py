from datetime import date
from pathlib import Path

import os

def save_entry(content: str):

    today = date.today().isoformat()

    BASE_DIR = Path(__file__).resolve().parent.parent
    
    notes_dir = BASE_DIR / "notes" 

    os.makedirs(notes_dir, exist_ok=True)

    file_path = f"{notes_dir}/{today}.md"

    markdown_content = f"""# Riyaz Entry

Date: {today}

## Learned Today

{content}
"""

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    return file_path
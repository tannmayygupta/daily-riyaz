from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_all_entries():

    notes_dir = BASE_DIR / "notes"

    entries = []

    for file in notes_dir.rglob("*.md"):

        with open(file, "r", encoding="utf-8") as f:
            markdown = f.read()

        relative = file.relative_to(notes_dir)

        date = (
            f"{relative.parts[0]}-"
            f"{relative.parts[1]}-"
            f"{relative.stem}"
        )

        entries.append({
            "date": date,
            "content": markdown
        })

    entries.sort(
        key=lambda x: x["date"],
        reverse=True
    )

    return entries
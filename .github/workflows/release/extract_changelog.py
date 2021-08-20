"""EXTRACT CHANGELOG Script
This script extracts the changelog for the given version from the CHANGELOG.md file.
The version is given as x.y.z (e.g. 0.1.1) as an arg (e.g. running "python extract_changelog.py 0.1.1").

The changelog is saved as markdown on a file, whose name/path can be configured
with the CHANGELOG_OUTPUT_FILE env variable (default to "changelog_generated.md").

The expected CHANGELOG.md file must have a format like the following:

```markdown
# Changelog

## 0.0.2

- Baz feature

## 0.0.1

- Foo feature
- Bar feature
```
"""

import os
import sys
import re
from typing import List

from markdown2 import markdown
from bs4 import BeautifulSoup

CHANGELOG_READ_FILE = "CHANGELOG.md"
CHANGELOG_OUTPUT_FILE = os.getenv("CHANGELOG_OUTPUT_FILE", "changelog_generated.md")


def _is_valid_version(version: str) -> bool:
    return bool(re.match(r"^(\d+\.)?(\d+\.)?(\*|\d+)$", version))


def _find_changelog_list(soup: BeautifulSoup, version: str) -> List[str]:
    version_header = soup.find("h2", text=version)
    if not version_header:
        print("Version header not found!")
        exit(1)

    changelog_list = version_header.find_next_sibling("ul")
    return [li.text.strip() for li in changelog_list.find_all("li")]


def _format_changelog_output(changelog: List[str]) -> str:
    output = ""
    for change in changelog:
        output += f"\n- {change}"
    return output.strip()


def _read(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def _save(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)


def extract_changelog(version: str):
    assert _is_valid_version(version)

    file_content = _read(CHANGELOG_READ_FILE)
    file_html = markdown(file_content)

    soup = BeautifulSoup(file_html, "html.parser")
    changelog_changes = _find_changelog_list(soup=soup, version=version)
    changelog_output = _format_changelog_output(changelog_changes)

    _save(filename=CHANGELOG_OUTPUT_FILE, content=changelog_output)


if __name__ == '__main__':
    extract_changelog(sys.argv[-1])

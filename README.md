# 🌐 StaticSite — Markdown to HTML Static Site Generator

A command-line static site generator built in Python that converts Markdown content
into a fully rendered HTML website — completed as part of the [Boot.dev](https://boot.dev)
Back-end Developer Path.

This is the most technically layered project in the portfolio: it involves recursive file
processing, custom Markdown parsing, HTML templating, and an automated test suite.

---

## ⚙️ What It Does

- Recursively copies a static asset directory to a public output folder
- Parses Markdown files and converts them to structured HTML
- Handles inline elements: bold, italic, code, links, and images
- Handles block elements: headings, paragraphs, lists, blockquotes, code blocks
- Applies a shared HTML template across all generated pages
- Runs via a shell script (`main.sh`) for a single-command build

---

## 🗂️ Project Structure

```
StaticSite/
├── src/               # Core Python source modules
│   ├── main.py            # Entry point — orchestrates the full generation pipeline
│   ├── htmlnode.py        # HTML node classes — LeafNode, ParentNode, rendering logic
│   ├── textnode.py        # Inline text node types (bold, italic, code, link, image)
│   ├── markdown_blocks.py # Block-level Markdown parsing (headings, lists, quotes)
│   ├── inline_markdown.py # Inline Markdown parsing (bold, italic, code, links)
│   └── copystatic.py      # Recursive static asset copying
├── main.sh            # Build script — runs the generator
├── test.sh            # Test runner — executes the full test suite
└── .gitignore
```

---

## 🧪 Testing

This project includes an automated test suite executed via shell script:

```bash
# Run all tests
./test.sh
```

Tests cover the core parsing and rendering logic — validating that Markdown input
produces correct HTML output across node types and block structures. This reflects
the same validation mindset applied professionally: define expected output, test
against actual output, catch regressions early.

---

## 🛠️ Skills Demonstrated

| Skill | Applied Where |
|---|---|
| Recursive file I/O | Static asset copying in `copystatic.py` |
| Custom parsing logic | Inline and block Markdown parsers |
| Class hierarchy | `HTMLNode` → `LeafNode` / `ParentNode` rendering tree |
| String processing | Regex-free inline delimiter parsing |
| Automated testing | `test.sh` test runner across parsing modules |
| Shell scripting | `main.sh` build orchestration |
| Separation of concerns | Each parsing concern isolated in its own module |

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Mikcec/StaticSite.git
cd StaticSite

# Build the site
./main.sh

# Run the test suite
./test.sh
```

**Requirements:** Python 3.x — no external dependencies.

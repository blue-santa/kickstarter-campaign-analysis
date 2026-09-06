import re
from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=2)

with open("capstone-03-project-report.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Force a page break immediately before every image so it never
# gets squeezed into leftover space on the current page.
md_content = re.sub(
    r'(!\[.*?\]\(.*?\))',
    r'<div style="page-break-before: always;"></div>\n\n\1',
    md_content
)

css = """
img {
    max-width: 100%;
    max-height: 90vh;
    height: auto;
    display: block;
    margin: 1em auto;
}
"""

pdf.add_section(Section(md_content), user_css=css)
pdf.save("output.pdf")

from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=2)

with open("capstone-03-project-report.md", "r", encoding="utf-8") as f:
    md_content = f.read()

css = """
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
}
"""

pdf.add_section(Section(md_content), user_css=css)
pdf.save("output.pdf")

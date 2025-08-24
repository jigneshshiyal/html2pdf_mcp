from weasyprint import HTML
from mcp.server.fastmcp import FastMCP
from jinja2 import Template
import tempfile
import os
import uuid

mcp = FastMCP("html2pdf_mcp", port=9000)

temp_dir = tempfile.gettempdir()

mcp.tool()
def html2pdf(html_code: str, data: dict = {}) -> str:
    """
    Convert HTML code to a PDF file.

    Args:
        html_code (str): The HTML code to be converted.
        data (dict, optional): A dictionary of data to be used in the HTML template. Defaults to an empty dictionary.

    Returns:
        str: return link to download the generated PDF file.
    """

    # Render the HTML template with the provided data
    template = Template(html_code)
    rendered_html = template.render(data)

    # Convert the rendered HTML to PDF
    pdf_bytes = HTML(string=rendered_html).write_pdf()

    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(temp_dir, filename)

    with open(filepath, "wb") as f:
        f.write(pdf_bytes)

    return f"/download/{filename}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
# app.py (Updated for New Template - CONOP Generator)

from flask import Flask, request, render_template, send_file
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_pdf():
    form_data = request.form

    reader = PdfReader("CONVENTION CONOP TEMPLATE 4 24 with data.pdf")
    writer = PdfWriter()
    writer.append(reader)

    # Fill out fields matching new template's exact field names
    writer.update_page_form_field_values(writer.pages[0], {
        "convention_name": form_data.get("convention_name", ""),
        "activity_description": form_data.get("activity_description", ""),
        "who": form_data.get("who", ""),
        "what": form_data.get("what", ""),
        "when": form_data.get("when", ""),
        "where": form_data.get("where", ""),
        "cost": form_data.get("cost", ""),
        "asset": form_data.get("asset", ""),
        "tair": form_data.get("tair", ""),
        "mac": form_data.get("mac", ""),
        "ppi": form_data.get("ppi", ""),
        "impressions": form_data.get("impressions", ""),
        "engagements": form_data.get("engagements", ""),
        "leads": form_data.get("leads", ""),
        "cois": form_data.get("cois", "")
    })

    # Force field appearances to render properly
    writer._root_object.update({
        NameObject("/NeedAppearances"): NameObject("true")
    })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)

    filename = f"conop-{datetime.now().strftime('%Y-%m-%d')}.pdf"
    return send_file(output, as_attachment=True, download_name=filename, mimetype="application/pdf")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)

# app.py (Updated for latest Template - April 2025 Version)

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

    reader = PdfReader("CONVENTION CONOP TEMPLATE 4 24 with data.pdf.pdf")
    writer = PdfWriter()
    writer.append(reader)

    # Updated field names to match April 2025 template
    writer.update_page_form_field_values(writer.pages[0], {
        "confrence_name": form_data.get("confrence_name", ""),
        "ACTIVITY DESCRIPTIONRow1": form_data.get("activity_description", ""),
        "who": form_data.get("who", ""),
        "what": form_data.get("what", ""),
        "when": form_data.get("when", ""),
        "where": form_data.get("where", ""),
        "POC": form_data.get("POC", ""),
        "asset": form_data.get("asset", ""),
        "tair": form_data.get("tair", ""),
        "MAC": form_data.get("mac", ""),
        "PPI": form_data.get("ppi", ""),
        "IMPRESSIONS": form_data.get("impressions", ""),
        "ENGAGEMENTS": form_data.get("engagements", ""),
        "LEADS": form_data.get("leads", ""),
        "COIs": form_data.get("COIs", "")
    })

    # Force appearance rendering
    writer._root_object.update({
        NameObject("/NeedAppearances"): NameObject("true")
    })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)

    filename = f"conop-{datetime.now().strftime('%Y-%m-%d')}.pdf"
    return send_file(output, as_attachment=True, download_name=filename, mimetype="application/pdf")

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


@app.route("/convention")
def convention():
    return render_template("convention.html")

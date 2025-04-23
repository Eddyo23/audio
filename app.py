from flask import Flask, request, render_template, send_file
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_pdf():
    form_data = request.form

    # Load the template PDF
    reader = PdfReader("Template.pdf")
    writer = PdfWriter()
    writer.append(reader)

    # Fill out the form fields from the HTML form
    writer.update_page_form_field_values(writer.pages[0], {
        "convention_name": form_data.get("convention_name", ""),
        "activity_description": form_data.get("activity_description", ""),
        "Who": form_data.get("Who", ""),
        "What": form_data.get("What", ""),
        "When": form_data.get("When", ""),
        "Where": form_data.get("Where", ""),
        "POC": form_data.get("POC", ""),
        "Asset": form_data.get("Asset", ""),
        "TAIR": form_data.get("TAIR", ""),
        "MAC": form_data.get("MAC", ""),
        "PPI": form_data.get("PPI", ""),
        "Impressions": form_data.get("Impressions", ""),
        "Engagements": form_data.get("Engagements", ""),
        "Leads": form_data.get("Leads", ""),
        "COI": form_data.get("COI", ""),
        "Cost": form_data.get("Cost", "")
    })

    # Force field appearances to render correctly
    writer._root_object.update({
        NameObject("/NeedAppearances"): NameObject("true")
    })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="conop.pdf", mimetype="application/pdf")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)

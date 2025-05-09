from flask import Flask, request, render_template, send_file
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, BooleanObject, DictionaryObject
import io

app = Flask(__name__)

# Home page (Landing)
@app.route('/')
def home():
    return render_template('index.html')

# Convention form
@app.route('/convention')
def convention():
    return render_template('convention.html')

@app.route('/generate', methods=['POST'])
def generate_pdf():
    form_data = request.form
    reader = PdfReader("CONVENTION CONOP TEMPLATE 4 24 with data.pdf.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        writer.update_page_form_field_values(page, {
            "activity_description": form_data.get("activity_description", ""),
            "who": form_data.get("who", ""),
            "what": form_data.get("what", ""),
            "when": form_data.get("when", ""),
            "where": form_data.get("where", ""),
            "poc": form_data.get("poc", ""),
            "asset": form_data.get("asset", ""),
            "tair": form_data.get("tair", ""),
            "mac": form_data.get("mac", ""),
            "impressions": form_data.get("impressions", ""),
            "engagements": form_data.get("engagements", ""),
            "leads": form_data.get("leads", ""),
            "coi": form_data.get("coi", ""),
            "activity_name": form_data.get("activity_name", ""),
            "personell": form_data.get("personell", ""),
            "uniform": form_data.get("uniform", ""),
            "hotel": form_data.get("hotel", ""),
            "notes": form_data.get("notes", "")
        })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return send_file(output, download_name="filled_template.pdf", as_attachment=True)

# After Action Review form
@app.route('/usarec-aar')
def show_usarec_form():
    return render_template('usarec_aar_form.html')

@app.route('/generate-aar', methods=['POST'])
def generate_aar_pdf():
    form = request.form
    reader = PdfReader("usarec_aar_template.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    field_data = {
        "event_title": form.get("event_title", ""),
        "event_mac": form.get("event_mac", ""),
        "actual_cost": form.get("actual_cost", ""),
        "mission_commander": form.get("mission_commander", ""),
        "pmc_email": form.get("pmc_email", ""),
        "pmc_phone": form.get("pmc_phone", ""),
        "item1": form.get("item1", ""),
        "qty1": form.get("qty1", ""),
        "item2": form.get("item2", ""),
        "qty2": form.get("qty2", ""),
        "item3": form.get("item3", ""),
        "qty3": form.get("qty3", ""),
        "item4": form.get("item4", ""),
        "qty4": form.get("qty4", ""),
        "item5": form.get("item5", ""),
        "qty5": form.get("qty5", ""),
        "item6": form.get("item6", ""),
        "qty6": form.get("qty6", ""),
        "tair_unit": form.get("tair_unit", ""),
        "tair_asset": form.get("tair_asset", ""),
        "impressions": form.get("impressions", ""),
        "cois": form.get("cois", ""),
        "prospects": form.get("prospects", ""),
        "vips": form.get("vips", ""),
        "recruiters": form.get("recruiters", ""),
        "rotc": form.get("rotc", ""),
        "again": form.get("again", ""),
        "display_location": form.get("display_location", ""),
        "description": form.get("description", ""),
        "challenges": form.get("challenges", ""),
        "well": form.get("well", ""),
        "improvement": form.get("improvement", ""),
        "reviewer": form.get("reviewer", "")
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, field_data)

    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })
    else:
        writer._root_object.update({
            NameObject("/AcroForm"): DictionaryObject({
                NameObject("/NeedAppearances"): BooleanObject(True)
            })
        })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return send_file(output, download_name="usarec_aar_filled.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

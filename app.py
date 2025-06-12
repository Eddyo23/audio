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
            "cois": form_data.get("cois", ""),
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





# Tour CONOP
@app.route('/tourconop')
def tourCONOP():
    return render_template('tourconop.html')

@app.route('/generate-tour', methods=['POST'])
def generate_tour_pdf():
    form_data = request.form
    reader = PdfReader("TourCONOP.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        writer.update_page_form_field_values(page, {
            "event_name": form_data.get("event_name", ""),
            "event_namepg2": form_data.get("event_namepg2", ""),
            "activity_description": form_data.get("activity_description", ""),
            "who": form_data.get("who", ""),
            "what": form_data.get("what", ""),
            "when": form_data.get("when", ""),
            "where": form_data.get("where", ""),
            "poc": form_data.get("poc", ""),
            "bn_poc": form_data.get("bn_poc", ""),
            "asset": form_data.get("asset", ""),
            
            "mac": form_data.get("mac", ""),
            "impressions": form_data.get("impressions", ""),
            "engagements": form_data.get("engagements", ""),
            "leads": form_data.get("leads", ""),
            "cois": form_data.get("cois", ""),
            "school1": form_data.get("school1", ""),
            "school2": form_data.get("school2", ""),
            "school3": form_data.get("school3", ""),
            "school4": form_data.get("school4", ""),
            "school5": form_data.get("school5", ""),
            "school6": form_data.get("school6", ""),
            "school7": form_data.get("school7", ""),
            "school8": form_data.get("school8", ""),
            "school9": form_data.get("school9", ""),
            "school10": form_data.get("school10", ""),
            "personell": form_data.get("personell", ""),
            "uniforms": form_data.get("uniforms", ""),
            "hotel1": form_data.get("hotel1", ""),
            "hotel2": form_data.get("hotel2", ""),
            "hotel3": form_data.get("hotel3", ""),
            "hotel4": form_data.get("hotel4", ""),
        })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return send_file(output, download_name="filled_template.pdf", as_attachment=True)




# Audition Tour
@app.route('/auditiontour')
def auditiontour():
    return render_template('auditiontour.html')

@app.route('/generate-auditiontour', methods=['POST'])
def auditiontourtemplate_pdf():
    form_data = request.form
    reader = PdfReader("auditiontourtemplate.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        writer.update_page_form_field_values(page, {
            "event_name": form_data.get("event_name", ""),
        
            "activity_description": form_data.get("activity_description", ""),
            "who": form_data.get("who", ""),
            "what": form_data.get("what", ""),
            "when": form_data.get("when", ""),
            "where": form_data.get("where", ""),
            "poc": form_data.get("poc", ""),
            "vehicle": form_data.get("vehicle", ""),
            
            
            
            "impressions": form_data.get("impressions", ""),
            "engagement": form_data.get("engagements", ""),
            "leads": form_data.get("leads", ""),
            
    
        })

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return send_file(output, download_name="auditiontourtemplate.pdf", as_attachment=True)



# AMPA Forms
@app.route('/ampa-forms')
def ampa():
    return render_template('ampa-forms.html')

@app.route('/download/9E-trombone')
def download_trombone_pdf():
    return send_file("9E-trombone.pdf", as_attachment=True)

@app.route('/download/9C-euphonium')
def download_euphonium_pdf():
    return send_file("9C-euphonium.pdf", as_attachment=True)

@app.route('/download/9B-trumpet')
def download_trumpet_pdf():
    return send_file("9B-trumpet.pdf", as_attachment=True)

@app.route('/download/9D-french horn')
def download_french_horn_pdf():
    return send_file("9D-french horn.pdf", as_attachment=True)

@app.route('/download/9F-tuba')
def download_tuba_pdf():
    return send_file("9F-tuba.pdf", as_attachment=True)

@app.route('/download/9G-flute')
def download_flute_pdf():
    return send_file("9G-flute.pdf", as_attachment=True)

@app.route('/download/9H-oboe')
def download_oboe_pdf():
    return send_file("9H-oboe.pdf", as_attachment=True)

@app.route('/download/9J-clarinet')
def download_clarinet_pdf():
    return send_file("9J-clarinet.pdf", as_attachment=True)

@app.route('/download/9K-bassoon')
def download_bassoon_pdf():
    return send_file("9K-bassoon.pdf", as_attachment=True)

@app.route('/download/9L-saxophone')
def download_saxophone_pdf():
    return send_file("9L-saxophone.pdf", as_attachment=True)

@app.route('/download/9M-percussion')
def download_percussion_pdf():
    return send_file("9M-percussion.pdf", as_attachment=True)

@app.route('/download/9N-keyboard')
def download_keyboard_pdf():
    return send_file("9N-keyboard.pdf", as_attachment=True)

@app.route('/download/9T-guitar')
def download_guitar_pdf():
    return send_file("9T-guitar.pdf", as_attachment=True)

@app.route('/download/9U-electric bass')
def download_electric_bass_pdf():
    return send_file("9U-electric bass.pdf", as_attachment=True)

@app.route('/download/9V-vocalist')
def download_vocalist_pdf():
    return send_file("9V-vocalist.pdf", as_attachment=True)

@app.route('/download/9X-music support technician')
def download_music_support_technician_pdf():
    return send_file("9X-music support technician.pdf", as_attachment=True)





# QPM Packets Routes

@app.route('/qpm-packets')
def qpm_packets():
    return render_template('QPM-Packets.html')

@app.route('/download/qpm/9b_trumpet_1')
def download_9b_trumpet_1():
    return send_file('QPM Packets/9B Trumpet QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9b_trumpet_2')
def download_9b_trumpet_2():
    return send_file('QPM Packets/9B Trumpet QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9c_euphonium_1')
def download_9c_euphonium_1():
    return send_file('QPM Packets/9C Euphonium QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9c_euphonium_2')
def download_9c_euphonium_2():
    return send_file('QPM Packets/9C Euphonium QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9d_horn_1')
def download_9d_horn_1():
    return send_file('QPM Packets/9D Horn QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9d_horn_2')
def download_9d_horn_2():
    return send_file('QPM Packets/9D Horn QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9e_bass_trombone_1')
def download_9e_bass_trombone_1():
    return send_file('QPM Packets/9E Bass Trombone QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9e_tenor_trombone_2')
def download_9e_tenor_trombone_2():
    return send_file('QPM Packets/9E Tenor Trombone QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9f_tuba_1')
def download_9f_tuba_1():
    return send_file('QPM Packets/9F Tuba QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9f_tuba_2')
def download_9f_tuba_2():
    return send_file('QPM Packets/9F Tuba QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9g_flute_1')
def download_9g_flute_1():
    return send_file('QPM Packets/9G Flute QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9g_flute_2')
def download_9g_flute_2():
    return send_file('QPM Packets/9G Flute QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9h_oboe_1')
def download_9h_oboe_1():
    return send_file('QPM Packets/9H Oboe QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9h_oboe_2')
def download_9h_oboe_2():
    return send_file('QPM Packets/9H Oboe QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9j_clarinet_1')
def download_9j_clarinet_1():
    return send_file('QPM Packets/9J Clarinet QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9j_clarinet_2')
def download_9j_clarinet_2():
    return send_file('QPM Packets/9J Clarinet QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9k_bassoon_1')
def download_9k_bassoon_1():
    return send_file('QPM Packets/9K Bassoon QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9k_bassoon_2')
def download_9k_bassoon_2():
    return send_file('QPM Packets/9K Bassoon QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9l_saxophone_1')
def download_9l_saxophone_1():
    return send_file('QPM Packets/9L Saxophone QPM 1 (2).pdf', as_attachment=True)

@app.route('/download/qpm/9l_saxophone_2')
def download_9l_saxophone_2():
    return send_file('QPM Packets/9L Saxophone QPM 2 (1).pdf', as_attachment=True)

@app.route('/download/qpm/9m_percussion_1')
def download_9m_percussion_1():
    return send_file('QPM Packets/9M Percussion QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9m_percussion_2')
def download_9m_percussion_2():
    return send_file('QPM Packets/9M Percussion QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9n_keyboard_1')
def download_9n_keyboard_1():
    return send_file('QPM Packets/9N Keyboard QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9n_keyboard_2')
def download_9n_keyboard_2():
    return send_file('QPM Packets/9N Keyboard QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9t_guitar_1')
def download_9t_guitar_1():
    return send_file('QPM Packets/9T Guitar QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9u_bass_1')
def download_9u_bass_1():
    return send_file('QPM Packets/9U Bass QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9u_bass_2')
def download_9u_bass_2():
    return send_file('QPM Packets/9U Bass QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9v_female_1')
def download_9v_female_1():
    return send_file('QPM Packets/9V Female QPM 1.pdf', as_attachment=True)

@app.route('/download/qpm/9v_female_2')
def download_9v_female_2():
    return send_file('QPM Packets/9V Female QPM 2.pdf', as_attachment=True)

@app.route('/download/qpm/9v_male_1')
def download_9v_male_1():
    return send_file('QPM Packets/9V Male QPM 1.pdf', as_attachment=True)


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


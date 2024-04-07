# app.py
import numpy as np
import pickle

from flask import (
    Flask,
    render_template,
    request
)
import secrets
from forms import PredictionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generate a 16-byte (32-character) hex token


@app.route('/')
def dashboard():
    team_members = [
        {
            'name': 'Masruk Habib',
            'email': 'masrukhabib.114214@marwadiuniversity.ac.in',
            'img_src': 'team_member_1.jpeg',
        },
        {
            'name': 'Puvanenthira Rajah',
            'email': 'puvanenthirarajah.sathasivam114232@marwadiuniversity.ac.in',
            'img_src': 'team_member_2.jpeg',
        },
        {
            'name': 'Wasihun Ageru Feleke',
            'email': 'wasihunagerufeleke.114083@marwadiuniversity.ac.in',
            'img_src': 'team_member_3.jpeg',
        },
        {
            'name': 'Prof. Ravikumar R N',
            'email': 'rnravikumar.cse@gmail.com',
            'img_src': 'team_member_4.jpeg',
        }
    ]
    return render_template('dashboard.html', team_members=team_members)


@app.route('/form', methods=['GET', 'POST'])
def report():
    current_page = "report"
    form = PredictionForm()
    age_sex = [form.age, form.sex]
    step1_fields = [
        form.on_thyroxine, form.q_on_thyroxine,
        form.on_anti_thyroid, form.sick,
        form.pregnant, form.thyroid_surgery,
        form.I131, form.query_hypothyroid,
        form.query_hyperthyroid, form.lithium, form.goitre,

    ]
    step2_fields = [
        [
            form.tumor,
            form.hypo_pituitary, form.psych
        ], [
            form.tsh_measured, form.tsh,
            form.t3_measured, form.t3,
            form.tt4_measured, form.tt4,
            form.t4u_measured, form.t4u,
            form.fti_measured, form.fti,
        ]
    ]
    return render_template(
        'report_form.html',
        step1_fields=step1_fields,
        step2_fields=step2_fields,
        age_sex=age_sex
    )


@app.route('/result', methods=['GET', 'POST'])
def result():
    print(len(request.form))
    print(request.form)
    form_data = request.form.copy()
    form_data.pop('submit', None)

    # Assign the remaining form data to mock_data
    mock_data = list(form_data.items())
    mock_data1 = list(form_data.values())
    print(mock_data)
    print(len(mock_data))
    print(mock_data1)
    print(len(mock_data1))

    input_data = [float(x) for x in mock_data1]
    np_data = np.array(input_data).reshape([1, -1])

    model = pickle.load(open("model.pkl", 'rb'))
    prediction = model.predict(np_data)
    print(prediction)

    text = 'Based on the provided data, the model predicts indications of hyperthyroidism.'
    text += 'Consultation with a healthcare professional is recommended for further evaluation and treatment.'
    title = 'Negative Prediction'
    if prediction == 0:
        text = 'The model does not detect any thyroid disorder based on the provided data.'
    elif prediction == 1:
        title = 'Hypothyroidism Prediction'
    elif prediction == 2:
        title = 'Hyperthyroidism Prediction'

    return render_template(
        'result.html',
        current_page='result',
        title=title,
        text=text
    )


if __name__ == '__main__':
    app.run(debug=True, port=3000)

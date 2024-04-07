# forms.py
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, EmailField, DateField, SelectField, FloatField, \
    IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class PredictionForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired()])

    sex = SelectField('Sex', choices=[('1', 'Male'), ('0', 'Female')], validators=[InputRequired()])
    on_thyroxine = SelectField('On Thyroxine', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    q_on_thyroxine = SelectField('Query on Thyroxine', choices=[('0', 'No'), ('1', 'Yes')],
                                 validators=[InputRequired()])
    on_anti_thyroid = SelectField('On Anti-thyroid Medication', choices=[('0', 'No'), ('1', 'Yes')],
                                  validators=[InputRequired()])


    sick = SelectField('Sick', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    pregnant = SelectField('Pregnant', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])

    thyroid_surgery = SelectField('Thyroid Surgery', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    I131 = SelectField('I131 Treatment', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])

    query_hypothyroid = SelectField('Query Hypothyroid', choices=[('0', 'No'), ('1', 'Yes')],
                                    validators=[InputRequired()])
    query_hyperthyroid = SelectField('Query Hyperthyroid', choices=[('0', 'No'), ('1', 'Yes')],
                                     validators=[InputRequired()])

    lithium = SelectField('Lithium', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    goitre = SelectField('Goitre', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    tumor = SelectField('Tumor', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    hypo_pituitary = SelectField('Hypo Pituitary', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    psych = SelectField('Psych', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])


    # Measured fields
    tsh_measured = SelectField('TSH Measured', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    tsh = FloatField('TSH', validators=[InputRequired()])

    t3_measured = SelectField('T3 Measured', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    t3 = FloatField('T3', validators=[InputRequired()])

    tt4_measured = SelectField('TT4 Measured', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    tt4 = FloatField('TT4', validators=[InputRequired()])

    t4u_measured = SelectField('T4U Measured', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    t4u = FloatField('T4U', validators=[InputRequired()])

    fti_measured = SelectField('FTI Measured', choices=[('0', 'No'), ('1', 'Yes')], validators=[InputRequired()])
    fti = FloatField('FTI', validators=[InputRequired()])

from flask import Flask, render_template, session, redirect, url_for
from flask.ext.wtf import Form
from wtforms import IntegerField, StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import Required
import pickle
from sklearn import datasets

# Initialize Flask App
app = Flask(__name__)


print "loading my model"
with open('model.pkl', 'rb') as handle:
    machine_learning_model = pickle.load(handle)
print "model loaded"


# Initialize Form Class
class theForm(Form):
    param1 = DecimalField(label='Sepal Length (cm):', places=2, validators=[Required()])
    param2 = DecimalField(label='Sepal Width (cm):', places=2, validators=[Required()])
    param3 = DecimalField(label='Petal Length (cm):', places=2, validators=[Required()])
    param4 = DecimalField(label='Petal Width (cm):', places=2, validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    print session
    form = theForm(csrf_enabled=False)
    if form.validate_on_submit():  # activates this if when i hit submit!
        # Retrieve values from form
        session['sepal_length'] = form.param1.data
        session['sepal_width'] = form.param2.data
        session['petal_length'] = form.param3.data
        session['petal_width'] = form.param4.data
        # Create array from values
        flower_instance = [(session['sepal_length']), (session['sepal_width']), (session['petal_length']),
                           (session['petal_width'])]

        # Return only the Predicted iris species
        flowers = ['setosa', 'versicolor', 'virginica']
        session['prediction'] = flowers[machine_learning_model.predict(flower_instance)[0]]

        # Implement Post/Redirect/Get Pattern
        return redirect(url_for('home'))

    return render_template('home.html', form=form, **session)


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.secret_key = 'super_secret_key_shhhhhh'
if __name__ == '__main__':
    app.run(debug=True)

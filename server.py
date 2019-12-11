import os
import csv
from flask import (Flask, 
                    render_template, 
                    send_from_directory, 
                    request, 
                    redirect
)
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

##Aşağıdaki şekilde de oluyor 
# ancak her yeni url yi bu şekilde eklemek gerekiyor.
# Bunun yerine yukarıdaki dynamic olanı kullanmak daha mantıklı.

#@app.route('/works.html')
#def my_works():
#    return render_template('works.html')

#@app.route('/about.html')
#def about_me():
#    return render_template('about.html')

#@app.route('/contact.html')
#def contact_me():
#    return render_template('contact.html')

#@app.route('/components.html')
#def my_components():
#    return render_template('components.html')

#@app.route('/work.html')
#def my_work():
#    return render_template('work.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
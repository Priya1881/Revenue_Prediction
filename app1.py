from prediction_service import prediction
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import os
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")


app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)
app.config['UPLOAD_PATH'] = 'uploads'
#app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv']

@app.route("/",methods=['GET','POST'])
def index():
      if request.method == 'POST' :

            try:

                            uploaded_file = request.files['file']
                            filename = secure_filename(uploaded_file.filename)
                            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                            print(filename)

                            response = prediction.form_response(filename)
                            return render_template("index1.html", response=response)


            except Exception as e:
                    error = {"error":e}
                    return render_template("404.html",error=error)
 
      else:
          return render_template('index1.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
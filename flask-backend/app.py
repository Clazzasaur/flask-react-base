from flask import Flask, render_template

app = Flask(__name__, static_url_path='',
                  static_folder='../react-frontend/build',
                  template_folder='../react-frontend/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("CATCH ALL")
    print(path)
    path_dir = "../react-frontend/build" #path react build
    if path != "" and os.path.exists(os.path.join(path_dir, path)):
        return send_from_directory(os.path.join(path_dir), path)
    else:
        return send_from_directory(os.path.join(path_dir),'index.html')

@app.route("/")
def hello():
    return render_template("index.html")

app.run()
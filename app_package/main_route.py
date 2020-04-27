from app_package import app

@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")

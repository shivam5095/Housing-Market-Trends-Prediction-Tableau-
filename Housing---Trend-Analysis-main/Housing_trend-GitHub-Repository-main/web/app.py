from flask import Flask, render_template

# Serve from the repo's templates/ and static/ folders.
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static",
)


@app.route("/")
def index():
    return render_template("home.html", active_page="home")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard")


@app.route("/about")
def about():
    return render_template("about.html", active_page="about")


if __name__ == "__main__":
    # Use 0.0.0.0 so it is reachable from other hosts in containerized environments.
    app.run(host="0.0.0.0", port=5000, debug=True)

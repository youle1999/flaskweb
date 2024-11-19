from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Redirect to page 1 if no "page" parameter is provided
    page = request.args.get("page", default=None)
    if not page:
        return redirect(url_for("index", page=1))

    try:
        page = int(page)
    except ValueError:
        return render_template("index.html", page=None, message="ページはありません。")

    if page < 1 or page > 5:
        return render_template("index.html", page=None, message="ページはありません。")

    return render_template("index.html", page=page, message=None)


if __name__ == "__main__":
    app.run(debug=True)

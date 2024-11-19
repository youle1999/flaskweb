from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate GCD using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@app.route("/", methods=["GET", "POST"])
def calculate_aspect_ratio():
    aspect_ratio = ""
    width = ""
    height = ""
    error_message = ""

    if request.method == "POST":
        try:
            width = int(request.form.get("width", 0))
            height = int(request.form.get("height", 0))
            
            if width > 0 and height > 0:
                divisor = gcd(width, height)
                aspect_ratio = f"{width // divisor}:{height // divisor}"
            else:
                error_message = "Both width and height must be positive numbers."
        except ValueError:
            error_message = "Please enter valid numbers."

    return render_template(
        "index.html",
        aspect_ratio=aspect_ratio,
        width=width,
        height=height,
        error_message=error_message,
    )

if __name__ == "__main__":
    app.run(debug=True)

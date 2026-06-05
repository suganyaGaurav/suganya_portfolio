# =========================================
# Flask Portfolio Application
# =========================================

from flask import Flask, render_template

# =========================================
# Flask App Initialization
# =========================================

app = Flask(__name__)

# =========================================
# Home Route
# =========================================

@app.route("/")
def home():
    return render_template("index.html")

# =========================================
# Run Application
# =========================================

if __name__ == "__main__":
    app.run(debug=True)
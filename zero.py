from flask import Flask, render_template
import os
app = Flask(__name__)


import numpy as np
S=3
A=4
D = np.zeros([S, A])
print(D)

@app.route("/")
def index():
    
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5300)))

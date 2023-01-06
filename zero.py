from flask import Flask
import os
app = Flask(__name__)


import numpy as np
S=3
A=4
D = np.zeros([S, A])
print(D)

@app.route("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5300)))

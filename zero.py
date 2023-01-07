from flask import Flask
import os
app = Flask(__name__)

def p():
import numpy as np
S=3
A=4
D = np.zeros([S, A])
print(D)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5300)))

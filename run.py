import os
from time_tracker import app
print(os.environ['PYTHONPATH'])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
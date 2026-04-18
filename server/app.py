from flask import Flask

app = Flask(__name__)

# List of models as required for the logic
existing_models = ["sedan", "suv", "truck", "coupe"]

# 1. Resource at "/"
@app.route('/')
def home():
    # 2. Displays "Welcome to Flatiron Cars"
    return "Welcome to Flatiron Cars"

# 3. Resource at "/<model>"
@app.route('/<model>')
def get_model(model):
    # 4. Success case
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
     # 5. displays  '/<model> route in browser
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(port=5555)
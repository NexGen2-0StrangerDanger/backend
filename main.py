from flask import Flask, request, jsonify
from db.db import register, login


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"message": "manas says hi to you all"})


@app.route("/get-logs", methods=["GET"])
def get_logs():
    return jsonify({"message": "logs will be put here"})


@app.route("/apply-rules", methods=["POST"])
def protect():
    try:
        data = request.get_json()
        rules = data.get("rules", []) 

        if not isinstance(rules, list):
            return jsonify({"error": "Rules should be a list"}), 400

        # TODO: Implement IP blocking logic here

        return jsonify({"message": f"Applied {len(rules)} rules"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get-patch-id/<packet_range>", methods=["POST"])
def add_rules(packet_range: str):
    # add rules based on rules
    return jsonify({"message": "Hello world"})


@app.route("/api/login", methods=["POST"])
def login_user():
    try:
        data = request.getjson()
        email = data.get("email", "")
        password = data.get("password", "")
        
        if not isinstance(email, str):
            return jsonify({"error": "Email should be a string"}), 400
        if not isinstance(password, str):
            return jsonify({"error": "Password should be a string"}), 400
        
        result = login(user=email, password=password)
        if result != "":
            return jsonify({"error": f"{result}"}), 400
        
        return jsonify({"message": "Login succesful"}), 200
    
    except e:
        return jsonify({"error": f"{e}"}), 400
    
    
@app.route("/api/register", methods=["POST"])
def register_user():
        try:
            data = request.getjson()
            email = data.get("email", "")
            password = data.get("password", "")
            
            if not isinstance(email, str):
                return jsonify({"error": "Email should be a string"}), 400
            if not isinstance(password, str):
                return jsonify({"error": "Password should be a string"}), 400
            
            result = register(user=email, password=password)
            if result != "":
                return jsonify({"error": f"{result}"}), 400
            
            return jsonify({"message": "Login succesful"}), 200
        
        except e:
            return jsonify({"error": f"{e}"}), 400
        

if __name__ == "__main__":
    app.run(port=6969, debug=True)
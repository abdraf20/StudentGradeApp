from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Student Grades Analytics API",
        "usage": "Send a POST request to /analyze or use GET /analyze?grades=90,80,70"
    })

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_grades():
    grades = []
    
    # التعامل مع البيانات سواء جاءت من الرابط أو من Json
    if request.method == 'GET':
        grades_str = request.args.get('grades', '')
        if grades_str:
            grades = [float(x) for x in grades_str.split(',')]
    elif request.method == 'POST':
        data = request.get_json()
        grades = data.get('grades', [])

    if not grades:
        return jsonify({"error": "No grades provided. Example: /analyze?grades=90,85,60"}), 400

    # المنطق الإحصائي (Statistics Logic)
    stats = {
        "count": len(grades),
        "average": sum(grades) / len(grades),
        "max_grade": max(grades),
        "min_grade": min(grades),
        "status": "Excellent" if (sum(grades) / len(grades)) >= 90 else "Good"
    }

    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
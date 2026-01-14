from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    stats = None
    students = []

    if request.method == 'POST':
        try:
            # استلام البيانات النصية من الحقل المخفي
            data_str = request.form.get('students_data')
            if data_str:
                # تحويل النص إلى قائمة بايثون
                students = json.loads(data_str)
                
                # استخراج العلامات فقط للحسابات
                grades = [s['grade'] for s in students]
                
                if grades:
                    # العثور على أفضل طالب
                    best_student = max(students, key=lambda x: x['grade'])

                    stats = {
                        "count": len(grades),
                        "average": round(sum(grades) / len(grades), 2),
                        "max": max(grades),
                        "min": min(grades),
                        "best_student": best_student['name']
                    }
        except Exception as e:
            print("Error:", e)

    return render_template('index.html', stats=stats, students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
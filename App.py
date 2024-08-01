from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/academics', methods=['GET', 'POST'])
def academics():
    if request.method == 'POST':
        # Logic for handling academic tracking data from the frontend
        data = request.get_json()
        # Perform any necessary actions based on the data
        result_message = f"Tracking Academic - Subject: {data['subject']}, Grade: {data['grade']}"
        return jsonify({'message': result_message})

    # Render the academics template for GET requests
    return render_template('academics.html')

@app.route('/mentalhealth', methods=['GET', 'POST'])
def mentalhealth():
    if request.method == 'POST':
        # Logic for handling mental health support data from the frontend
        data = request.get_json()
        # Perform any necessary actions based on the data
        result_message = f"Supporting Mental Health - Emotion: {data['emotion']}, Activity: {data['activity']}"
        return jsonify({'message': result_message})

    # Render the mentalhealth template for GET requests
    return render_template('mentalhealth.html')

@app.route('/interests', methods=['GET', 'POST'])
def interests():
    if request.method == 'POST':
        # Logic for handling interests exploration data from the frontend
        data = request.get_json()
        # Perform any necessary actions based on the data
        result_message = f"Exploring Interests - Interest: {data['interest']}"
        return jsonify({'message': result_message})

    # Render the interests template for GET requests
    return render_template('interests.html')

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':
        # Logic for handling recommendation data from the frontend
        data = request.get_json()
        # Perform any necessary actions based on the data
        result_message = f"Recommendations - Academic Performance: {data['academic_performance']}, Mental Health: {data['mental_health']}, Interest: {data['interest']}"
        return jsonify({'message': result_message})

    # Render the recommendations template for GET requests
    return render_template('recommendations.html')

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        # Logic for generating personalized summary
        # Perform any necessary actions
        result_message = 'Generating Personalized Summary'
        return jsonify({'message': result_message})

    # Render the summary template for GET requests
    return render_template('summary.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Logic for handling feedback data from the frontend
        data = request.get_json()
        # Perform any necessary actions based on the data
        result_message = f"Feedback submitted: {data['feedbackText']}"
        return jsonify({'message': result_message})

    # Render the feedback template for GET requests
    return render_template('feedback.html')

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)

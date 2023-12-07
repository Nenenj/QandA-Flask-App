from flask import Flask, render_template, request

app = Flask(__name__)

def ask_question(question, expected_answer):
    user_response = request.form.get('answer')
    return user_response.lower() == expected_answer.lower()

# List of questions and answers
qa_pairs = [
    ("What is the capital of France? ", "Paris"),
    ("Which programming language is known for its readability and versatility? ", "Python"),
    ("In which year did World War II end? ", "1945"),
    ("What is the largest mammal in the world? ", "Blue Whale"),
    ("Who wrote 'Romeo and Juliet'? ", "William Shakespeare"),
    ("What is the currency of Japan? ", "Yen"),
    ("What is the square root of 64? ", "8"),
    ("Who is known as the 'Father of Computer Science'? ", "Alan Turing"),
    ("What is the chemical symbol for gold? ", "Au"),
    ("Which planet is known as the 'Red Planet'? ", "Mars"),
    ("Who painted the Mona Lisa? ", "Leonardo da Vinci"),
    ("What is the speed of light in a vacuum? (in km/s) ", "299792"),
    ("What is the largest ocean on Earth? ", "Pacific Ocean"),
    ("Which element has the symbol 'O'? ", "Oxygen"),
    ("Who developed the theory of relativity? ", "Albert Einstein"),
    # Add more questions and answers as needed
]

@app.route('/')
def index():
    return render_template('index.html', qa_pairs=qa_pairs)

@app.route('/qanda', methods=['POST'])
def qanda():
    answer = request.form.get('answer')
    question = request.form.get('question')
    for q, expected_answer in qa_pairs:
        if question == q and ask_question(question, expected_answer):
            return render_template('result.html', answer=answer, correct=True)
    return render_template('result.html', answer=answer, correct=False)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

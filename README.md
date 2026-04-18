# Driving Theory Test - Ôn thi GPLX B2

A web-based driving theory test application for learners studying for the Vietnamese GPLX B2 license.

## Features
- **600 Questions**: Comprehensive database of all 600 official driving theory questions.
- **Real-time Feedback**: Immediate validation of answers with correct highlighting.
- **Critical Questions**: Highlighted "Câu điểm liệt" (critical questions) with automatic fail logic.
- **Explanations**: Clear tips and explanations for each answer.
- **Responsive Design**: Mobile-friendly premium UI.

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript

## How to Run
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open in browser: `http://127.0.0.1:5000`

## Project Structure
- `app.py`: Flask server and API endpoints.
- `questions.json`: Structured question data.
- `templates/`: HTML frontend.
- `On-thi-gplx-hang-b2-2023.pdf`: Source material (image-based).

Disease Prediction App using Prompt Engineering with ChatGPT
Abstract
This project demonstrates how Generative AI tools like ChatGPT can be used for rapid prototyping of real-world machine learning applications. Instead of manually writing every line of code, the developer leveraged prompt engineering techniques to iteratively generate, debug, and refine Python scripts, Flask APIs, and HTML templates. The final product is a disease prediction system powered by a machine learning model trained on the Pima Indians Diabetes Dataset, deployed as a web application.
Introduction
With the rise of Large Language Models (LLMs), software development is being transformed. Developers can now guide AI systems to generate functional code through carefully designed prompts. This project explores the use of ChatGPT as a coding partner, where the role of the developer shifts from writing code to designing effective prompts and validating outputs.
Methodology
1. Prompt Engineering Process
- Initial prompt: 'Build a Flask app for disease prediction using a trained model.'
- Iterative refinements: Added requirements for HTML UI, error handling, confidence score, and JSON API.
- Debugging: When the model always predicted 'No Disease,' prompts were refined to adjust threshold logic and input preprocessing.
2. Code Generation
- ChatGPT generated Python code for Flask backend, HTML templates for the frontend, and guidance for requirements.txt.
- The developer validated and tested each component, refining prompts to resolve issues.
3. Deployment
- Final system includes app.py, index.html, and model.pkl.
- Supports both web form input and JSON API predictions.
Results
- A fully functional disease prediction system was created without manually coding each component.
- Demonstrates how LLMs accelerate development through guided prompting.
- The project highlights the effectiveness of prompt engineering in building production-like applications.
Conclusion
This project showcases the power of prompt engineering in software development. By guiding ChatGPT with precise prompts, a complete machine learning application was developed, tested, and deployed in significantly less time than traditional coding.
Future Work
- Explore advanced prompting strategies (chain-of-thought, role-based prompts).
- Compare AI-generated code with manually written implementations for performance and maintainability.
- Extend to other domains: NLP apps, recommendation systems, generative AI projects.




Installation & Setup
1️⃣ Clone this repository
git clone https://github.com/your-username/disease-prediction-app.git
cd disease-prediction-app
2️⃣ Create a Virtual Environment (recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Flask App
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000
Example Inputs
- Pregnancies: 2
- Glucose: 160
- Blood Pressure: 72
- Skin Thickness: 20
- Insulin: 85
- BMI: 32.5
- Diabetes Pedigree Function: 0.45
- Age: 45

Prediction: ✅ Disease Present (Confidence ~82%)

LinkedIn : https://www.linkedin.com/in/nischinth-k-510918263/


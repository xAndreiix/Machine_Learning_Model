# 🎵 Music Recommendation ML Model

---

## 📋 Table of Contents
- 🏷️ [Project Description](#project-description)
- ✨ [Features](#features)
- 🛠️ [Technologies](#technologies)
- 🗂️ [Project Structure](#project-structure)
- ⚙️ [Requirements](#requirements)
- 💾 [Installation](#installation)
- ▶️ [Usage](#usage)
- 🧪 [Running Tests](#running-tests)
- 🫱🏻‍🫲🏼 [Contributing](#contributing)
- 📜 [License](#license)
- 👨🏻‍💻 [Author](#author--acknowledgments--contact) / 🙏🏻 [Acknowledgments](#author--acknowledgments--contact) / 📩 [Contact](#author--acknowledgments--contact)
- 💰 [Support Me!](#if-you-want-to-support-me)

---

## Project Description
Simple machine learning project that demonstrates how to train, visualize, and export a music recommendation model using Python.  
The dataset maps user attributes such as age and gender to a preferred music genre.  
The project uses a decision tree classifier to make predictions and exports the trained model for reuse.
<!-- ## Badges -->
<!-- ## Live Demo -->
<!-- ## Screenshots -->

---

## Features
- Load and preprocess a CSV dataset
- Train a Decision Tree Classifier
- Export the trained model using `joblib`
- Visualize the tree structure with Graphviz
- Make predictions for new inputs

---

## Technologies
- Python
- NumPy
- Pandas
- scikit-learn
- PyTest
- Joblib
- Graphviz
- Jupyter Notebook

---

## Project Structure
- │ 📁 Music Recommendation ML Model/
- ├── data/
- │   └── music.csv
- ├── notebooks/
- │   └── Music_Recommendation_Machine.ipynb
- ├── models/
- │   └── music-recommender.joblib
- ├── visuals/
- │   └── music_recommender.dot
- ├── tests/
- │   └── test_model.py
- ├── requirements.txt
- ├── README.md
- ├── LICENSE
- └── .gitignore

---

## Requirements
- Python 3.10+
- Dependencies listed in [requirements.txt](requirements.txt)

---

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/xAndreiix/Machine_Learning_Model.git
```
```bash
cd Music_Recommendation_Model
```
```bash
pip install -r requirements.txt
```

---

## Usage
Open the Jupyter notebook to train and test the model:
```bash
jupyter notebook notebooks/Music_Recommendation_Machine.ipynb
```
Alternatively, load the pre-trained model in Python:
```bash
import joblib

model = joblib.load("models/music-recommender.joblib")
pred = model.predict([[21, 1]])  # Example: age=21, male
print(pred)
```
The model will output the predicted music genre based on the input data.

---

## Running Tests
```bash
pytest
```
```bash
pytest -v
```
<!-- ## Deployment -->
<!-- ## Notes -->
<!-- ## Road Map -->
<!-- ## FAQ -->

---

## Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.
<!-- ## Changelog -->

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE)

---

## Author / Acknowledgments / Contact
**Author:** 
Andrei Iliescu

[![Website](https://img.shields.io/badge/Website-PORTFOLIO-gold?style=for-the-badge&logo=about-dot-me&logoColor=white)](https://xandreiix.github.io/Andrei-Iliescu-Portfolio/)

**Acknowledgments:**  
- Inspired by [Mosh Hamedani's](https://www.youtube.com/@programmingwithmosh) tutorial on YouTube.

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=_uQrJ0TkZlc&ab_channel=ProgrammingwithMosh)
- All thanks to him for the training and examples!

**Contact:**  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/andrei-iliescu-aa7910214)<br>
[![Email Yahoo](https://img.shields.io/badge/Email-andrey_iliescu%40yahoo.com-6001D2?style=for-the-badge&logoColor=white)](mailto:andrey_iliescu@yahoo.com)<br>
[![Email Gmail](https://img.shields.io/badge/Gmail-andrei.iliescu13102000%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:andrei.iliescu13102000@gmail.com)

---

## If you want to support me
[![PayPal](https://img.shields.io/badge/PayPal-xAndreiix-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/xAndreiix)<br>
[![Revolut](https://img.shields.io/badge/Revolut-xAndreiix-001B2E?style=for-the-badge&logoColor=white)](https://revolut.me/xandreiix)
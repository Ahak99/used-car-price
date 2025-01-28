# 🚗 **Used Car Price Prediction Web Application**

## 🎯 Objectives

1. This project aims to predict the price of used cars based on various features and attributes. The target variable is the price, measured in lakhs.
2. The solution is implemented as a user-friendly **web application** for ease of use.
3. The application is **containerized with Docker** and deployed to **Heroku** for cloud hosting.

## 🛠️ Tools & Technologies Used

### 1. **Programming Language**: Python 🐍  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/77eb34b4-d758-4f70-bbf9-4cde54ced129" alt="Alt Text">
</div>

### 2. **Data Storage**: Amazon S3 ☁️  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/6d920e5e-ad0d-43cc-889f-91123fdf2d56" alt="Amazon S3 Logo">
</div>

### 3. **Machine Learning Libraries**:  
- **TensorFlow** ⚡  
- **Keras** 🧠  
- **Scikit-learn** 📚  
- **Pandas** 📊

<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/fae06a0b-7055-4c42-85f0-3a424bad9bef" alt="ML Libraries">
</div>

### 4. **Web Framework**: Flask 🖥️  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/df49ee4b-7b5c-4ad1-b23a-afe9e5c5c967" alt="Flask Logo">
</div>

### 5. **Containerization**: Docker 🐋  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/69fef606-0c05-48dd-9829-ee618887f797" alt="Docker Logo">
</div>

### 6. **Version Control**: GitHub 🧑‍💻  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/308b6f2c-6e69-4c92-b210-9d82b2d257e3" alt="GitHub Logo">
</div>

### 7. **Cloud Deployment**: Heroku 🌐  
<div align="center">
  <img src="https://github.com/Ahak99/used-car-price/assets/101395769/eb3aba47-aba8-4972-8fef-b9d30490cc31" alt="Heroku Logo">
</div>

---

## 🔄 Project Life Cycle

1. **Install Dependencies**  
   Install all necessary libraries for the project.

2. **Data Collection**  
   - **Dataset Source**: [Used Car Prices - Kaggle](https://www.kaggle.com/datasets/sujay1844/used-car-prices)  
   - The dataset is stored on **Amazon S3** for easy access.

3. **Data Preprocessing & Exploration**  
   - Perform data checks:
     - Missing values ❓
     - Duplicates ⚠️
     - Data types 🔢
     - Unique values 🔄
     - Descriptive statistics 📊
     - Categories in categorical columns 🗂️
   - **Data Analysis & Visualization** (more details in the notebook)

4. **Model Building**  
   - Split data into **training** and **testing** sets.
   - Normalize the data 📈.
   - Train the model and use **random search** to tune the best hyperparameters.
   - Save the model for future use 🗄️.
   - Make predictions with the trained model 🔮.

5. **Web Application Development**  
   - A **Flask-based web application** is developed for user interaction.

6. **Containerization**  
   - **Docker** is used to containerize the web application for easier deployment.

7. **Version Control**  
   - Push the project to **GitHub** for version control.

8. **CI/CD Pipeline**  
   - **GitHub Actions** is used for automated deployment and testing.

9. **Cloud Deployment**  
   - Deployed on **Heroku** for seamless hosting and scaling.

---

## 🖥️ Project Architecture

![Project Design](https://github.com/Ahak99/used-car-price/assets/101395769/183e7494-753c-4ec5-bda5-00de17eda571)

---

## 💻 Software & Tool Requirements

1. **GitHub** - For version control and repository management.
2. **IDE** - Any IDE of your choice (e.g., **VSCode**, **PyCharm**).
3. **Heroku Account** - To deploy and host the application on the cloud.

---

## 🧑‍💻 Setting Up the Development Environment

### 1. **Create a Virtual Environment**
```bash
python -m venv .venv

---

### 2. **Activate the Virtual Environment**
- On **Windows**
```bash
.venv\Scripts\activate

---

- On **macOS/Linux**
```bash
source .venv/bin/activate

---

## 🚀 Run the Application

1. **Install the required dependencies**  
   To install the necessary libraries, use the following command:

   ```bash
   pip install -r requirements.txt

---

2. **Run the Flask app**

```bash
   python app.py

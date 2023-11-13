# Used Car Price 

### Objectives
    1. The provided contains various details and attributes associated with used cars. The target variable, which is the central focus of analysis, is the price of the used cars, and it is measured in lakhs.
    2. To solve the problem statement, I opted to develop a user-friendly web application.
    3. Then I containerise it using Docker and deploy it on the heroku cloud.

### Tools & technologies used
    1. Programming language : Python
![python](https://github.com/Ahak99/used-car-price/assets/101395769/77eb34b4-d758-4f70-bbf9-4cde54ced129)
    2. Data storage : Amazon S3
![S3](https://github.com/Ahak99/used-car-price/assets/101395769/6d920e5e-ad0d-43cc-889f-91123fdf2d56)
    3. ML libraries : Tensorflow, Keras, Sklearn, pandas
![AI librairies](https://github.com/Ahak99/used-car-price/assets/101395769/fae06a0b-7055-4c42-85f0-3a424bad9bef)
    4. Docker
![docker](https://github.com/Ahak99/used-car-price/assets/101395769/69fef606-0c05-48dd-9829-ee618887f797)
    5. Github
![Github](https://github.com/Ahak99/used-car-price/assets/101395769/308b6f2c-6e69-4c92-b210-9d82b2d257e3)
    6. Heroku    
![heroku](https://github.com/Ahak99/used-car-price/assets/101395769/eb3aba47-aba8-4972-8fef-b9d30490cc31)

### Life cycle of project
    1. Install the dependencies
    2. Collect data
        - Dataset source : Dataset Source - https://www.kaggle.com/datasets/sujay1844/used-car-prices
        - The dataset was stored in Amazon S3.
    3. Read data
    4. Data Checks to perform
        - Check Missing values.
        - Check Duplicates.
        - Check data type.
        - Check the number of unique values of each column.
        - Check statistics of data set.
        - Check various categories present in the different categorical column.

    3. Data Analysis & Visualisation (more details in the notebook)

    5. Model building
        - Split data into Training/Testing set
        - Normalize data.
        - Train the model and use the random search method to select the best set of parameters.
        - Save the model
        - Predict

    6. Containerising the web application using Docker

    7. Push the project to GitHub

    8. Develop a CI/CD pipeline using GitHub actions

    9. Deploy the project to Heroku 

### Project design 
![Project Design](https://github.com/Ahak99/used-car-price/assets/101395769/183e7494-753c-4ec5-bda5-00de17eda571)

### Software and tools requirements

    1. Github
    2. Any IDE to work (VScode, PyCharm ...)
    3. Heroku account

# Used Car Price 

### Objectives
    1. The provided contains various details and attributes associated with used cars. The target variable, which is the central focus of analysis, is the price of the used cars, and it is measured in lakhs.
    2. To solve the problem statement, I opted to develop a user-friendly web application.
    3. Then I containerise it using Docker and deploy it on the heroku cloud.

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

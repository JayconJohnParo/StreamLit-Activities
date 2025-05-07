Streamlit Activities Collection

This repository contains 6 hands-on Streamlit activities given by our instructor, John Deloso Paulin, for our ITBAN2 (IT Business Analytics 2) course. These projects cover key concepts such as user interface interaction, data processing, API integration, database connectivity, and real-time computer vision using OpenCV—each designed to reinforce our understanding of practical data applications.

📘 Activities Overview I. 🚀 Hello, Streamlit!

Objective: Understand basic components of a Streamlit app.

Explanation: This project is a simple introduction to Streamlit where we create a basic interactive application. The app uses st.title, st.header, and st.write to display introductory text and instructions. The main functionality revolves around two input fields: one for entering a name (st.text_input) and the other for entering the user’s age (st.number_input). Based on the input, the app provides dynamic feedback. If a name is entered, a personalized greeting is displayed along with the user’s age. If the name field is empty, a warning is shown, prompting the user to enter their name. This project highlights how Streamlit can be used to quickly gather user input and display dynamic responses using simple widgets.

Screenshot:

![Capture](https://github.com/user-attachments/assets/c2c24de3-7d81-4a00-89d0-5c4d9ac48388)

II. 🧾 DataFrame Viewer

Objective: Load and display CSV data interactively.

Explanation: In this project, users can upload a CSV file using Streamlit’s st.file_uploader widget. Once the file is uploaded, it is read into a pandas DataFrame, which is then displayed on the app using st.dataframe. The project provides an option to filter the data based on specific columns, which are dynamically populated into a st.selectbox. Users can interactively choose a column and a value to filter the data. The application includes a feature to display raw data with a toggleable st.expander and ensures that the uploaded CSV file contains a minimum of 5 columns for better usability. This project demonstrates the powerful integration of Streamlit with pandas to quickly visualize and filter data in real-time.

Screenshot: 
![activity2](https://github.com/user-attachments/assets/18cfa868-6561-442c-b1d5-001bc1568707)

![activity2 sumpay](https://github.com/user-attachments/assets/12ff22b0-ce1b-4e55-8404-e39546e8cdc0)


III. 🧩 Sidebar and Layout

Objective: Organize content using Streamlit layout components.

Explanation: This project uses Streamlit’s layout components such as st.sidebar, st.columns, st.tabs, and st.expander to create an interactive and informative dashboard. The sidebar allows users to select topics related to data warehousing, ETL processes, and enterprise data management, while a slider controls the importance level of each topic. The main content is divided into columns to explain key concepts, such as data warehousing architecture and the ETL process. Interactive tabs provide additional information on definitions and real-world use cases, offering users a structured way to navigate through the material. The st.expander component allows users to explore additional information about these practices, making it an engaging learning tool for data professionals.

Screenshot:

![Capture](https://github.com/user-attachments/assets/239d36a0-b3f3-4608-8503-d38f83fc4c71)

![Capture 2](https://github.com/user-attachments/assets/15987832-d9cf-40bf-946f-ddc1bc9d836b)

![Capture 3](https://github.com/user-attachments/assets/fa94983d-7cf0-40cf-b52b-2f291ecdc706)




IV. 🌐 Fetch and Display API Data

Objective: Retrieve and visualize data from an external API.

Explanation: In this activity, we connect to a public API, such as Open-Meteo, using Python’s requests library to fetch live weather data. The data retrieved is in the form of JSON, which is then parsed and displayed in an interactive dashboard using Streamlit. The dashboard offers a variety of visualizations, such as line charts for temperature, bar charts for precipitation, and area charts for wind speed. Additionally, other charts like histograms and pie charts provide insight into the humidity distribution and weather conditions, respectively. This allows users to explore and analyze real-time weather forecasts in an organized and engaging way. Streamlit widgets like st.line_chart, st.bar_chart, and st.area_chart enhance the data presentation, while options for raw data inspection via st.expander offer deeper exploration.

Screenshot:

![cap1](https://github.com/user-attachments/assets/392ce9d3-d16f-4eca-8ac0-e29f5cc236da)

![cap2](https://github.com/user-attachments/assets/78a20da1-b5e9-4509-bba2-dbb16457e531)

![cap3](https://github.com/user-attachments/assets/126807c2-9795-449c-84f6-208782587e83)


![cap4](https://github.com/user-attachments/assets/c4a6cca8-6dae-4da2-9296-65d4d0ab91f6)


![cap5](https://github.com/user-attachments/assets/8ae79b30-9960-4548-802b-1d2ddd1a189c)


V. Data Pipeline with Database Demonstrates how Streamlit can interact with a MySQL database. Users can view and insert data using a form-based interface. A secure login system restricts access, showing how to combine Streamlit with authentication and backend services.

Screenshot:

![ika 5 1](https://github.com/user-attachments/assets/56d87f74-4f4b-4f29-8e87-f09066b3c72f)


![ika 5 2](https://github.com/user-attachments/assets/98c1d015-59fc-451c-a946-ace254698c93)

VI. 📹 Real-Time Video Stream with OpenCV

Objective: Display live webcam feed inside a Streamlit app.

Explanation: This activity demonstrates the use of OpenCV to capture video frames from a webcam and apply an Edge Preserving Filter. This filter is designed to smooth the image while preserving important edge details, creating a stylized, cartoon-like effect. It’s particularly useful for enhancing visual clarity without losing the structure of the image. In this implementation, the user can interactively control the intensity of the effect using sliders in the sidebar that adjust the spatial (sigma_s) and range (sigma_r) filtering parameters.

Screenshot and Snapshot:

![snapshot_1746629170](https://github.com/user-attachments/assets/501cf64e-6eea-4c0b-80cf-d1fa1e24843b)

![Capture](https://github.com/user-attachments/assets/caa69a8b-c9d1-47c0-8553-bbc605c86a6c)

![Capture 1](https://github.com/user-attachments/assets/0c79b481-a5b7-4bb1-865d-eb3e6f5dcb97)












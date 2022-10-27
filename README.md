# Square Root Microservice README.md
## Step by step process on how to implement
### 1. Install rpyc
- Locate your project interpreter. In python the path is File > New Project Settings > Settings for New Projects... > Python Interpreter
- Select the python interreter you are using for this prject [ex. (Python 3.8 C:\Users...)]
- Select the + icon in the top right corner
![image](https://user-images.githubusercontent.com/72044353/198372448-081c3cbc-b417-4e7c-9203-f9344c288a20.png)
- Search rpyc and install package
![image](https://user-images.githubusercontent.com/72044353/198372595-d44ca321-62a8-4b7f-84ea-144b9971931b.png)

### 2. Create an rpyc connection to server on your client
- Import rpyc in your client file

![image](https://user-images.githubusercontent.com/72044353/198372960-460493cf-baf4-4351-9eb2-708704494007.png)

- Create connection to the server

![image](https://user-images.githubusercontent.com/72044353/198373436-080a96b1-0fa9-4010-a6ce-caa7e4e39e5c.png)

### 3. Request and Receive data

- Call the microservice whenever it is needed using the sample code here

![image](https://user-images.githubusercontent.com/72044353/198373640-f8d60b14-a4fe-4ad5-8f9e-2917030c25c4.png)

- The command will return the square root of the number provided

### 3. Run squareroot_service.py before your client file and you are good to go!
![image](https://user-images.githubusercontent.com/72044353/198375457-d61413a4-f73e-4dd5-97cf-2cf78e9f8711.png)

## Common Errors
### 1. Make sure you're selecting the right python interpreter
- You may have several python interpreters to select from previous projects, make sure you're selecting the general one
![image](https://user-images.githubusercontent.com/72044353/198375942-3fc6962a-a36f-44ae-8533-bb8bdc65fb6e.png)

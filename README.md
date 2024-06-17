                                                    A Full Report On Project

Name of Project: Basic Bank Application

Name of Developer: IKECHUKWU NWAMAH

Description: This is a full stack bank application built with next js as the frontend and django as it's back end. The application is set to enable users make transfers, withdraw money and also deposit into their app. Each time a user makes a transaction on the app, the transaction history is updated showing the user what kind of transaction was done, this way it can enable users to keep track of every transaction done and also for security purposes should in case a transaction is done without their consent. During the deployment, the frontend and backend were deployed seperately so that once the backend was deployed, the complete api link was fed in the frontend in other to make my api consumable to the frontend

Tools/Technologies: There are mulitiple tools and technologies employed in developing this project. The technologies are specified both on the frontend and on the bankend and also deployment technologies where utilized in this project. The tools therefore can be stated as thus:
Frontend Tools/Technologies: Javascript, Tailwind css, Nextjs framework, Jsonwebtoken, autoprefixer, Jwt_decode further techologies can be found in the package.json at the root directory of the frontend project
Backend Tools/Technologies: Python, Django, corsheaders, graphene, Rsa, Mongoengine, Inflection, Jinja, Websocket, Drf-yasg, Djongo, Promise, Packaging, Django, Djangorestframework, Djangorestframework-simplejwt, npm-axios, heroku, gitlab. Further technologies can also be found in the requirements.txt at the root directory of the project

Method of Development: On the backend, first thing was to connect the django framework to a mongodb database cluster using the mongoengine/pymogo for local testing, then i went further to set up my django, and django rest framework. After registering in the settings.py of my project, I started implementation by creating seperate apps for my project and then routing them to a common project urls.py. So that once being routed, the apis can be fetched at each call on the endpoint. The signup api is developed to send otp to users so that they can easily verify their account which was handled on the frontend. On the frontend: The various forms were created and each of the forms consumed the apis being fetched on the backend. This access token is also being retrieved on the frontend and stored in a local storage was was implemented also, while the access token is stored, a jwt decorder was implemented to decode the token before it is then being used to access the particular section of the application. It was develped so that only authenticated users can have access to the app, therefore the user must first be logged in simultanously generate an access token in other for the user to gain complete access to the app. The access token generated was implemented on the backend to automatically be saved on the header request for each call to the api using a middleware encryption system which was implemented in the project path

How to Set Up Project: Django like every other python framework expects you always have a virtual environment as a best practice, virtual environments allows developers to run multiple dependecies on a single machine without causing a clash with themselves, therefore its best practice to always have a virtual environment. To create a virtual environment, you first check that python is installed on your machine, then you run the command "python -m venv <name of environment>". After the environment has been successfully created, you activate it by running the script "<source <name of environment>/bin/activate" This command immediately activates the virtual environment. Because a requirement.txt is already included in the project directory, so you could easily run this script "<pip install -r requirements.txt>" this scripts immediately installs all the dependecies found in my requiremets.txt. You could either clone the existing project to your system, and after setting up the virtual environment, then you activate and move the cloned environment to your already set up environment, then you run the latter script command to install all dependecies. But on the frontend, once the project is cloned, you can run the <npm install> to install all the packages found on the package.json. Following this steps helps you set up the project on your system. The next line talks about how to run the project.

How to Run Project: Every project has a software development lifecycle which is called the SDLC, and this cycle talks about how a project goes from the development stage to the production stage. 
On the development stage for the backend: The project was run using the command : ./manage.py runserver, you can also set a default ip and port by modifying the command ./manage.py runserver 127.0.0.1:8000. This command enables the application to run on this ip while listening to this port. 
For the frontend, the commad to run the application is npm run dev, this automatically runs your project to next development server, then you can access the various UIs that has been developed.
On the production stage for the backend: The project was first pushed to a version control called gitlab, in which from their i was able to effectively deploy to render by setting up a continous integration and continous deployment(CI/CD) which was implemented at the root of my project directory. In that CI, the commands to build, test and run my backend and frontend were implemented, also implemented were commands to automatically install all dependecies and technologies used in the project which were defined in the requirements.txt for the backend and package.json on the frontend. While to test the backend you use the "./manage.py test" command and for the frontend you use the npm test command.


Challenges Encountered While Developing: Ofcourse there were challenges i encountered during this few days of development, the challengies therefore are:
1. Setting up a working CI/CD. This was an issue in the sense that the job kept failing each time i implement but i didn't let it stop me, i still pressed on to make sure the project was up to a notable standard while finding ways around the obstacle
2. Lack of constant power supply: This was a major issue, though it posed as a challenge, i still had to find my way around it to make sure the project was as expected.
3. Handling daily activities coupled with the project: This was also a challenge, i teach software engineering, python programming and cyber security. Therefore, i had to reschedule my time just so i can be able to also fulfil some/all the requirements of this projects since it is a full stack project.
4. Mongo Db Challenge: This held me for days, trying to make my mongodb cloud server communicate with my render since render was used to deploy my apis. I even went ahead to feed the ips that render offers for communication to the mongodb network access yet to no avail, then on reading the project requirements a second time, i then realized that since graphql was incorporated in this project, i am not entirely restricted to just using mongodb, therefore i decided to use the postgresql offered by render. 

Vote of Thanks: This was really an awesome project and i am so glad that i participated in the project. My sincere appreciation goes to veegil for first considering me for this role, then secondly opening me up to some fun technologies and implementation. To the hr for deeming it fit to be explicit enough while dishing out the requirements of the project, so that once i skimmed through it, i was able to pick out what was being requested. I am already excited about joining the team but the decision still lies within the organization, not withstanding. Thank you VEEGIL!!!

Link to Deployed Project:  
Django Deployed Links: https://bankapp-hd3c.onrender.com
base_url = https://bankapp-hd3c.onrender.com
APi Links: 
Graphql Api Links:
withdrawgraphql: {base_url}/api/v1/withdrawgraphql
Depositgraphql: {base_url}/api/v1/depositgraphql
Transfergraphql: {base_url}/api/v1/transfergraphql
ProfileGraphql: {base_url}/api/v1/profilegraphql
Transaction-HistoryGraphql: {base_url}/api/v1/transactionhistorygraphql
RegisterGraphql:{base_url}/api/v1/registergraphql
LoginGraphql: {base_url}/api/v1/logingraphql
BalanceGraphql: {base_url}/api/v1/balancegraphql

Rest Api Links
Deposit:{base_url}/api/v1/deposit/
Withdraw: {base_url}/api/v1/withdraw
Transfer: {base_url}/api/v1/transfer-money
Profile: {base_url}/api/v1/profile
Transaction-Hisory: {base_url}/api/v1/transaction-history
Register: {base_url}/api/v1/auth/register
Login: {base_url}/api/v1/auth/login
Balance: {base_url}/api/v1/balance




Swagger Documetations for Rest Apis:
Swagger(For rest apis): https://bankapp-hd3c.onrender.com/swagger/?format=openapi



Frontend Deployed Link:
Vercel:
https://minibank.vercel.app/

Default Admi Login To See Database:
email: ike@gmail.com
password: issac

Local Ip Address For Django
http://127.0.0.1:8000/

Local Ip Address For Nextjs
http://localhost:3000/






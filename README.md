# RecipeGenius
This project is the implementation of a knowledge database for a topic that is very near and dear to all our hearts (and stomachs): food. That's right, food; the lifesource of humanity. It is thus envisioned to be a place where people can. We have started it off by scraping from the Food Network website recipe database a wide variety of world foods and their recipes. Thus, we already have a pre-populated database of many foods ready so that users are not stuck with creating endless amounts of recipes or waiting for others to do so in order to get the most from this app. 

The main components of this project are Django for the backend/middle-end, a MongoDB database to store the recipes (in JSON format, of course), and some flavor of JavaScript for the frontend (most likely Angular). For now, the codebase and all other materials will be stored on Amazon Web Services (AWS) instances. One instance contains the Django code and one is for the MongoDB database (the frontend will likely be on the same instance as the Django code).

In order to run the project, perform the following steps:
1. Turn on the AWS instances from the EC2 dashboard
2. Open Terminal
3. Login into the AWS instance(s) using the following command ''ssh -i <locationofKeyPairFile>/myKeyPair.pem ubuntu@<publicIPaddress>''. The <locationofKeyPairFile> <publicIPaddress> field is contained in the information page of the EC2 instance. For instance, if my key pair file is in my Documents directory on a Mac (or any flavor of Linux) and the public IP is 34.24.567.89, then the command I would run is ''ssh -i ./Documents/myKeyPair.pem ubuntu@34.24.567.89''.

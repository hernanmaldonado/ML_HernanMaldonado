packages required: 
	fastapi 0.110.1
	pydantic2.6.4 (pydantic is included with fast API as of the creation fo this file)
	torch2.2.1
	networkx3.2.1

To launch the api in docker you need to run docker and the following commands:  
	Make sure docker is running
	Run the following commands in the locatioin wqhere the docker 
	docker build -t namegen .
	docker run -d --name mycontainer -p 80:80 namegen
	
Then visit: http://127.0.0.1:80/items/10 to get 10 names. 
You can change the number after "items" in the above web address to get a different set of names or press enter at the address bar. 
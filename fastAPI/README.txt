packages required: 
	fastapi 0.110.1
	pydantic2.6.4 (pydantic is included with fast API as of the creation fo this file)
	torch2.2.1
	networkx3.2.1

To launch the api you need to type the below command in the same folder as the fastAPI files are: 
	python -m uvicorn main:app --reload
Then visit: http://127.0.0.1:8000/items/10 to get 10 names. 
You can change the number after "items" in the above web address to get a different set of names or press enter at the address bar. 
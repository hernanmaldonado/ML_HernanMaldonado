# nameGen: A Probabilistic Graph Approach to GenAI

This project is based in Andrej Karpathy's [makemore](https://github.com/karpathy/makemore). His project uses different approaches from bigrams to deeplearning and transformers. My approach is to use a probabilistic graph instead. 
I decided to try this approach because I thought I could build an efficient model with a small footprint with high performance.  

nameGen shows my creativity to come up with a different approach to a problem and solve it in an efficient yet innovative way without sacificing performance. 

## Set-up
nameGen has three different deploymement methods you can try.
1. CLI: you can downlowd the CLI files **install the libraries** that are referenced on teh README file on theat folder and try namGen yourself.
   The fastest version is makeMoreGraph_v3.py, it uses a pickle file with the graph already created and ready to create new names. To run it all you need to do is type:
    
   ```
   python makeMoreGraph_v3.py
   ```
2. fastAPI: This version of nameGen showcases the creation of an API to use the app. The basic commands to run the API are:
   ```
   python -m uvicorn main:app --reload
   ```
  Then visit: http://127.0.0.1:8000/items/10 to get 10 names. 
     
3. docker: This version is to showcase the ease of use of the library in a dockerized API. The commands to run the docker container are:
  ```
 	docker build -t namegen .
	docker run -d --name mycontainer -p 80:80 namegen
  ```

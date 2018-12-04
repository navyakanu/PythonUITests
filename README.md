# PythonUITests
Sample selenoid usage for python UI tests

Sample Application under test:

    http://www.google.com

How to run the tests?

    ./run_test.sh --test_type=only --with_docker=true
    
    
What does ./run_test.sh contain and do?

1) Brings up the virtual environment for python3.6
2) Use docker-compose to bring up selenoid and selenoid UI, you can access 
    the selenoid-ui with the below URL
    
        http://localhost:8081/

3) Make sure you pull the docker images for the browser images mentioned in the browsers.json and configure according to the 
    requirements

4) All the videos recorded are saved in /video in the PWD (Videos are saved with the session id)



    

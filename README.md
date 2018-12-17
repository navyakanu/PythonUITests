# PythonUITests
Sample selenoid usage for python UI tests (Based on the documentation from the selenoid page)

Sample Application under test:

    http://www.google.com

How to run the tests?

    ./run_test.sh --test_type=only 
    
    
What does ./run_test.sh contain and do?

1) Brings up the virtual environment for python3.6
2) Use docker-compose to bring up selenoid and selenoid UI, you can access 
    the selenoid-ui with the below URL
    
        http://localhost:8081/

3) Make sure you pull the docker images for the browser images mentioned in the browsers.json and configure according to the 
    requirements
    To quickly do this install jq (brew install jq)
    Run the command 
    
        cat /path/to/browsers.json | jq -r '..|.image?|strings' | xargs -I{} docker pull {}    
    
4) All the videos recorded are saved in /video in the PWD (Videos are saved with the session id)

5) If you are changing or updating browsers.json, restart docker image for selenoid, otherwise you docker would not recognise the environment



    
    
# hivery-backend-challenge
Rest API built to fetch the desired information of people in Paranuara

This solution is tested on both Linux and Windows operating systems. While the order of execution remains same, syntaxes may vary with respect to versions of operating systems.

1. Clone the git repo and change the current directory to hivery-backend-challenge

    ```sh
    $ git clone https://github.com/sashiy/hivery-backend-challenge.git
    $ cd hivery-backend-challenge
    ```

2. Create and activate virtualenv, if bin directory is unavilable please look for Scripts directory inside hivery and then activate the virtual environment

    ```sh
    $ virtualenv hivery
    $ source hivery/bin/activate
    ```

    > **NOTE**: You know that you are in a virtual environment as "hivery" is now showing before the $ in your terminal - (hivery)$. To exit the virtual environment, use the command `deactivate`. You can reactivate by navigating back to the project directory and running `source hivery/bin/activate`.

3. Install all the dependencies listed in requirements.txt 

    ```sh
    (hivery)$ pip install -r requirements.txt
    ```

4. Run the application (Different JSON files can be used by changing the paths of COMPANIES_JSON & PEOPLE_JSON at paranuara_api/main/config.py)

    ```sh
    (hivery)$ python manage.py runserver
    ```
    
    Endpoints:
    
    1. Get employees in a company
       Expected Input: Name of a company (ex: KIGGLE)
       Expected Output: Employees of KIGGLE, attributes displayed include (name, age, address, phone)
       URL: http://127.0.0.1:5000/company/KIGGLE
    
    2. Get favourite food of a person
       Expected Input: _id of a person (ex: 595eeb9badcc6df8cff78f5d)
       Expected Output: Persons favourite food distinguished by fruits and vegetables, attributes displayed include (name, age, favourite fruits, favourite vegetables)
       URL: http://127.0.0.1:5000/people/595eeb9badcc6df8cff78f5d
      
    3. Get common friends between two people
       Expected Input: _id of a person 1 and _id of person 2 (ex: 595eeb9badcc6df8cff78f5d,595eeb9b71e64ebde0ade1ad)
       Expected Output: Friends in common for both person 1 and person2 who are still alive and have brown eyes, attributes displayed include (name, age, address, phone) of person 1, person 2 and all the friends in common meeting the criteria
       URL: http://127.0.0.1:5000/people/595eeb9b71e64ebde0ade1ad/595eeb9badcc6df8cff78f5d

    
    
5. Run all test cases (While test cases remain same, input criteria must be changes in case of using different companies.json or people.json)

    ```sh
    (hivery)$ python manage.py test
    ```


    ```
 
    

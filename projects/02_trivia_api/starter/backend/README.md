# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference
-   Introduction
-   Getting Started
    .   Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as proxy in the frontend configuration.
    .   Authentication: This version of the application does not require authentication or API keys.

-   Error
    Erros are returned as JSON objects in the following format:
    {
         "success": False,
          "error": 404,
          "message": "resource not found"
    }
    The API will return five error types when requests fail:
    .   400: Bad Request
    .   404: Resource Not Found
    .   422: Not Processable
    .   405: Method Not Found
    .   500: Internal Server Error

-   Endpoints
    GET /categories
    .   General:
        .   Returns a dictionary of categories, success value, and total number of categories
    .   Sample: curl http://127.0.0.1:5000/categories
        {
        "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
        }, 
        "success": true, 
        "total_categories": 6
        }
    GET /questions
    .   General:
        .   Returns a list of question objects, a dictionary of categories,  success value, total question number
        .   Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    .   Sample:  curl http://127.0.0.1:5000/questions

        {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "questions": [
            {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 1, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            }, 
            {
            "answer": "George Washington Carver", 
            "category": 4, 
            "difficulty": 2, 
            "id": 12, 
            "question": "Who invented Peanut Butter?"
            }, 
            {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer's original name is Cassius Clay?"
            }, 
            {
            "answer": "Scarab", 
            "category": 4, 
            "difficulty": 4, 
            "id": 23, 
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            }, 
            {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }, 
            {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            }, 
            {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            }, 
            {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 11, 
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }, 
            {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 13, 
            "question": "What is the largest lake in Africa?"
            }
        ], 
        "success": true, 
        "total_questions": 36
        }

    
    DELETE /questions/<question_id>
    .   General: delete a question by <question_id>
        .   Returns a list of question objects,deleted question id,  success value, total question number
        .   Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    .   Sample: curl -X DELETE http://127.0.0.1:5000/questions/1
        {
        "deleted": 1, 
        "questions": [
            {
            "answer": "George Washington Carver", 
            "category": 4, 
            "difficulty": 2, 
            "id": 12, 
            "question": "Who invented Peanut Butter?"
            }, 
            {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer's original name is Cassius Clay?"
            }, 
            {
            "answer": "Scarab", 
            "category": 4, 
            "difficulty": 4, 
            "id": 23, 
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            }, 
            {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }, 
            {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            }, 
            {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            }, 
            {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 11, 
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }, 
            {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 13, 
            "question": "What is the largest lake in Africa?"
            }, 
            {
            "answer": "The Palace of Versailles", 
            "category": 3, 
            "difficulty": 3, 
            "id": 14, 
            "question": "In which royal palace would you find the Hall of Mirrors?"
            }
        ], 
        "success": true, 
        "total_questions": 35
        }


    POST /add
    .   General:
        .   Create an question using the submitted question, answer, difficulty and category. Returns success value, created question id, question and the total question number.
        .   curl -X POST -H "Content-Type: application/json" -d '{"question":"testing", "answer":"testing","category":1, "difficulty":1,"id":38}' http://127.0.0.1:5000/add
       
        {
        "error": 422, 
        "message": "cannot process request although it's properly formatted", 
        "success": false
        }
    
    POST /questions
    .   General:
        .   Search an question which contains search term input by user. Returns success value, questions contain search terms and total number of questions which contain search terms.
        .   curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"soccer"}' http://127.0.0.1:5000/questions

        {
        "questions": [
            {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 11, 
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }
        ], 
        "success": true, 
        "total_questions": 2
        }
    
    GET /categories/<category_id>
    .   General:
        .   Returns the questions of given category_id, current_category, success value and total question number of current category
        .   curl -X GET http://127.0.0.1:5000/categories/2/questions

        {
        "current_category": 2, 
        "questions": [
            {
            "answer": "Escher", 
            "category": 2, 
            "difficulty": 1, 
            "id": 16, 
            "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            }, 
            {
            "answer": "Mona Lisa", 
            "category": 2, 
            "difficulty": 3, 
            "id": 17, 
            "question": "La Giaconda is better known as what?"
            }, 
            {
            "answer": "One", 
            "category": 2, 
            "difficulty": 4, 
            "id": 18, 
            "question": "How many paintings did Van Gogh sell in his lifetime?"
            }, 
            {
            "answer": "Jackson Pollock", 
            "category": 2, 
            "difficulty": 2, 
            "id": 19, 
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            }, 
            {
            "answer": "The Baroque period", 
            "category": 2, 
            "difficulty": 2, 
            "id": 36, 
            "question": "Name the extravagant period of art and architecture prevalent in Europe during most of the 17th century?"
            }, 
            {
            "answer": "Leonardo Da Vinci", 
            "category": 2, 
            "difficulty": 2, 
            "id": 37, 
            "question": "Which famous painter was also a sculptor, an architect, and an engineer?"
            }
        ], 
        "success": true, 
        "total_questions": 6
        }

    
    POST /quizzes
    .   General
        .   this endpoint take category and return a random question within the given category, current category and success value
        .   curl -X POST -H 'Content-Type: application/json' -d '{"previous_questions": [],"quiz_category":{"type":"Geography","id": "2"}}' http://127.0.0.1:5000/quizzes

        {
        "current_category": "Geography", 
        "question": {
            "answer": "Jackson Pollock", 
            "category": 2, 
            "difficulty": 2, 
            "id": 19, 
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            }, 
        "success": true
        }

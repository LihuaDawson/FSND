import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
      page = request.args.get('page',1,type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE

      questions = [question.format() for question in selection]
      current_questions = questions[start:end]

      return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app)
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
      response.headers.add('Access-Control-Allow-Methods','GET,POST,PATCH,DELETE,OPTIONS')
      return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  curl -X GET http://127.0.0.1:5000/categories
  '''
  @app.route('/categories')
  def get_categories():
        categories = {category.id: category.type for category in Category.query.all()}

        return jsonify({
          'success': True,
          'categories': categories,
          'total_categories': len(categories)
        })
  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions')
  def get_questions():
        questions = Question.query.all()
        categories = {category.id: category.type for category in Category.query.all()}
        formatted_questions = paginate_questions(request,questions)

        if(len(formatted_questions) == 0):
              abort(404)

        return jsonify({
          'success': True,
          'questions': formatted_questions,
          'total_questions': len(questions),
          'categories':categories
        })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>',methods=['DELETE'])
  def delete_question(question_id):
        try:
          question = Question.query.filter(Question.id == question_id).one_or_none()
          if question is None:
                abort(404)
          
          question.delete()
          selection = Question.query.all()
          current_questions = paginate_questions(request,selection)

          return jsonify({
            'success': True,
            'deleted': question_id,
            'questions': current_questions,
            'total_questions': len(selection)
          })
        except:
          abort(422)
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/add',methods=['POST'])
  def add_question():
      body = request.get_json()
      question = body.get('question',None)
      answer = body.get('answer', None)
      category = body.get('category', None)
      difficulty = body.get('difficulty', None)

      try:
          question = Question(question = question, answer = answer,category = category, difficulty = difficulty)
          question.insert()

          selection = Question.query.all()
          current_question = paginate_questions(request,selection)

          return jsonify({
            'success': True,
            'created': question.id,
            'questions': current_question,
            'total_question': len(selection)
          })
      except Exception as e:
        print('Exception >> ', e)
        abort(422)
        
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions',methods=['POST'])
  def search_question():
        
        try:
          body = request.get_json()
          search_term = body.get('searchTerm','')
          if search_term:
              questions = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
              current_questions = paginate_questions(request,questions)

              return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),

            })
          else:
                return jsonify({
                  'success':False,
                  'reason':'search term not there'
                })
                
        except:
          abort(422)
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions',methods=['GET'])
  def get_questions_by_category(category_id):
      try:
        questions = Question.query.filter(Question.category == category_id).all()
        current_questions = paginate_questions(request,questions)

        return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(questions),
          'current_category': category_id
        })
      except:
        abort(422)
        
        


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 

  curl -d '{"previous_questions": [],"quiz_category": {"type":"Geography",
  "id": "2"}}' -H 'Content-Type: application/json' -X POST 
  http://127.0.0.1:5000/quizzes
  '''

  @app.route('/quizzes',methods=['POST'])
  def play_quiz():
      
      quiz_category = request.json.get('quiz_category')
      previous_questions = request.json.get('previous_questions')

      try:
        if quiz_category:
              if quiz_category['id'] == 0:
                  print("quiz_category exits here on line 232!")
                  questions = Question.query.all()
                  
              else:
                  print("line 234 quiz_category is not all ")
                  questions = Question.query.filter(Question.category == quiz_category['id']).all()
              if not questions:
                  print("question not exist here on 239!")
                  return abort(422)
             
              quizzes = [quiz for quiz in questions if quiz.id not in previous_questions]
              quiz = random.choice(quizzes)
              print("before return joson")
              print("the random quiz: ", quiz)
              print("random quiz on format: ", quiz.format())
              return jsonify({
                  'success': True,
                  'question':quiz.format(),
                  'current_category': quiz_category['type']
        })
        else:
              abort(404)
              
      except:
        abort(422)
      # return jsonify({
      #   'success': True,
      #   'quiz_category':quiz_category,
      #   'questions': questions,
      #   'previous_questions':previous_questions 
      # })


       
        
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
          "success": False,
          "error": 422,
          "message": "cannot process request although it's properly formatted"
        }), 422

  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
        }),400

  @app.errorhandler(405)
  def method_not_found(error):
        return jsonify({
          "success": False,
          "error": 405,
          "message":"Method Not Allowed"
        }),405

  @app.errorhandler(500)
  def internal_server_error(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "Internal Server Error"
        }),500
  
        
  return app

    
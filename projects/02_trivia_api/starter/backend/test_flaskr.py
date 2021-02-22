import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.add_question = {
            'question':'testing question',
            'answer':'testing answer',
            'difficulty':1 ,
            'category':1
        }

        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'],36)
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['questions']),10)
    
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=200')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')
    
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']),6)
    
    def test_add_question(self):
        res = self.client().post('/add', json=self.add_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        question_id = data['created']
        self.client().delete('/questions/'+str(question_id))
        

    def test_delete_question(self):
        question = Question(question='question to delete', answer='answer to delete', category=1,difficulty =1)
        question.insert()
        question_id = question.id
        res = self.client().delete('/questions/'+str(question.id))
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == question.id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'],question_id)
        self.assertTrue(len(data['questions']))
        self.assertEqual(question, None)
    
    def test_search_question_with_result(self):
        res = self.client().post('/questions', json={'searchTerm':'soccer'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['questions'],True)
        self.assertTrue(data['total_questions'],2)
    
    def test_search_question_without_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'melon'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['questions'],[])
        self.assertEqual(data['total_questions'],0)

    def test_get_questions_by_category(self):
        res = self.client().get('categories/'+str(2)+'/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['total_questions'],6)
        self.assertEqual(data['current_category'],2)

    def test_quiz(self):
        res = self.client().post('/quizzes', json={'quiz_category':{'type': 'Science', 'id': '1'}, 'previous_questions':[]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['question'])
        self.assertEqual(data['current_category'],'Science')

      

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
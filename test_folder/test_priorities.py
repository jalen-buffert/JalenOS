import pytest 
from fastapi import FastAPI
from unittest import TestCase
from unittest.mock import patch
from fastapi.testclient import TestClient
from server.main import app
from server.data import real_priorities



# Testing Priority.py
class TestPriorityRoutes(TestCase):
    #Get all Priorities 
    def test_all_priorities(self):
        client = TestClient(app)
        response = client.get("/priorities/")
        self.assertEqual(response.status_code, 200)
    #Get specific priority by ID 
    def test_get_1_priority(self):
        client = TestClient(app)
        response = client.get("/priorities/1234")
        self.assertEqual(response.status_code,404) 
        
        
    
    #Create a new priority
    
    #Update a priority
    
    #Delete a priority
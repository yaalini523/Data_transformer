import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from input_reader.local_reader import read_file
from unittest.mock import patch

class TestLocalReader(unittest.TestCase):
    def setUp(self):
        self.test_folder = "test_input"
        os.makedirs(self.test_folder, exist_ok=True)
        
        self.test_file = "sample.json"
        
        self.sample_data = {
            "first_name":"Priya",
            "last_name":"Singh",
            "phone":"+91-9992462216"
        }
        
        with open(os.path.join(self.test_folder,self.test_file), "w") as f:
            json.dump(self.sample_data, f)
    
    
    @patch('input_reader.local_reader.input_path', new='test_input')
    def test_read_file(self):
        result = read_file()
        
        self.assertEqual(len(result), 1)
        
        self.assertEqual(result[0]["first_name"], "Priya")
        self.assertEqual(result[0]["phone"], "+91-9992462216")
      
    def tearDown(self):
        os.remove(os.path.join(self.test_folder, self.test_file))
        os.rmdir(self.test_folder)
    
if __name__ == "__main__":
    unittest.main()
    
        
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
import unittest
from unittest.mock import patch
from output_writer.local_writer import write_output

class TestLocalWriter(unittest.TestCase):
    def setUp(self):
        self.test_folder = "test_output"
        self.test_file = "sample.json"
        
        self.sample_data = {
            "first_name":"Priya",
            "last_name":"Singh",
            "phone":"+91-9992462216"
        }
        
    @patch("output_writer.local_writer.output_path", new="test_output")
    def test_write_file(self):
        write_output(self.sample_data, self.test_file)
        
        full_path = os.path.join(self.test_folder, self.test_file)
        self.assertTrue(os.path.exists(full_path), "Output file not created")
        
        with open(full_path, 'r') as f:
            result = json.load(f)
            
        self.assertEqual(result, self.sample_data)
    
    def tearDown(self):
        os.remove(os.path.join(self.test_folder, self.test_file))
        os.rmdir(self.test_folder)

if __name__ == "__main__":
    unittest.main()
        
        
        


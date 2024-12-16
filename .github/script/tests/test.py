# Imports
import re
from pathlib import Path
import shutil
import os
import sys

# Variables
from config import VERBOSE

# Functions
from files.images import fill_failed_images
from report.generate import generate_report
from files.parse import parse_markdown_files
from tests.evaluate import evaluate_tests

def validate_test_report():
    expected_test_report_path =  Path(__file__).resolve().parents[1] / 'report/expected_test_report.md'
    actual_test_report_path = Path(__file__).resolve().parents[1] / 'report/actual_test_report.md'
    with open(expected_test_report_path, 'r') as f1, open(actual_test_report_path, 'r') as f2:
        expected_test_report_content = f1.read()
        actual_test_report_content = f2.read()

    if expected_test_report_content == actual_test_report_content:
        return True
    else:
        return False

"""
Runs the tests for the pipeline
"""
def test():
    global SRC_DIR, DEST_DIR, REPORT_PATH

    SRC_DIR = Path(__file__).resolve().parents[0] / 'test_cases'
    DEST_DIR = Path(__file__).resolve().parents[0] / 'test_cases_build'
    REPORT_PATH = "./github/script/report/actual_test_report.md"

    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
        os.mkdir(DEST_DIR)

    parse_markdown_files(SRC_DIR, DEST_DIR, True) 
    
    fill_failed_images(SRC_DIR, DEST_DIR) 
    generate_report(REPORT_PATH) 

    if validate_test_report():
        if VERBOSE: print("Test report validation successful")
        if evaluate_tests():
            if VERBOSE: print("Test evaluation successful")
            sys.exit(0)
        else : 
            if VERBOSE: print("Test evaluation failed")
            sys.exit(1)  
    else : 
        if VERBOSE: print("Test report validation failed")
        sys.exit(1)
    

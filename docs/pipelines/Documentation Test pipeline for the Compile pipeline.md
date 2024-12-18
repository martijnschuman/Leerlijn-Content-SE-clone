
This GitHub Actions pipeline is designed to test scripts and configurations when changes are made to the `.github/` directory. It ensures that all necessary tests are executed in a clean environment.

## Purpose
- Runs automated tests whenever changes are pushed to the **`content` branch**.
- Focuses specifically on changes made to files within the `.github/` directory.
- Verifies content processing scripts by executing test cases.

## Workflow Overview
### Trigger
The pipeline is triggered on **pushes to the `content` branch** when files in the `.github/` directory are modified.

### Job: `runs-tests-on-pipeline`
This job ensures the testing pipeline is executed on an **`ubuntu-latest`** environment.

### Steps
1. **Configure Git**
	Sets up Git with a default user for committing changes.
	
2. **Checkout Code**
	Checks out the repository to ensure access to the latest `content` branch.
	
3. **Set Up Python**
	Installs Python 3.x to run necessary scripts.
	
4. **Install Dependencies**
	Installs required Python libraries (`pandas`, `openpyxl`) for content processing.
	
5. **Checkout Content Branch**
	Ensures the pipeline works with the latest `content` branch files.
	
6. **Run Test Script**
	Executes `run_tests.py`, which processes content and generates reports.
	*Script location:* `.github/script/tests/run_tests.py`.

## File Locations
- **Test Script**: `.github/script/tests/run_tests.py`

## Dependencies
- Python 3.x
- Required libraries:
    - `pandas`
    - `openpyxl`

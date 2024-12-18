
This GitHub Actions pipeline automates the process of compiling content, generating reports, and syncing them between the branches `content` and `staging`.

## Purpose
- Automatically compile and process content when changes are pushed to the `content` branch.
- Generate content reports and synchronize them to the `staging` branch.
- Streamline the workflow for handling content updates across multiple environments.

## Workflow Overview
### Trigger
The pipeline runs automatically when changes are pushed to the `content` branch.
It ignores changes inside the `.github/` directory.
### Permissions
- **Write access** to `contents` and `pull-requests` to allow pushing updates to branches.

## Job: `process-and-sync`
### Environment
- Runs on `ubuntu-latest`.
- Utilizes Python 3.x for script execution.

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
	
6. **Run Content Compilation Script**
	Executes `compile_content.py`, which processes content and generates reports.
	*Script location:* `.github/script/compile_content.py`.
	
7. **Copy Reports to Root**
	Copies the generated reports:
	- `content_report.md`
	- `taxco_report.md`
	
8. **Move Build Folder to Root**
	Moves the compiled build output to a new `build` folder at the root level.
	
9. **Commit Reports to `content` Branch**
	Adds the generated reports back to the `content` branch.
	Commits only if changes are detected.
	
10. **Sync to `staging` Branch**
	Switches to the `staging` branch to synchronize the build and reports:
	- Removes the old `build/` folder.
	- Copies the new `build/` folder and reports (`content_report.md` and `taxco_report.md`).
	- Commits and pushes the changes.

## File Locations
- **Content Compilation Script**: `.github/script/compile_content.py`
- **Generated Reports**:
- `content_report.md`
- `taxco_report.md`

## Branch Workflow
- **`content` Branch**:
- Trigger branch where changes are compiled and reports are generated.
- Reports (`content_report.md`, `taxco_report.md`) are committed to this branch.
- **`staging` Branch**:
- Receives the updated `build/` folder and reports for further processing or deployment.

## Dependencies
- Python 3.x
- Required libraries:
    - `pandas`
    - `openpyxl`


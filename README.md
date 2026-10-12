# First CI Demo — Student Result System

## Project Overview

This project demonstrates Continuous Integration (CI) using Python, unit testing, and GitHub Actions.

The application predicts whether a student passes or fails based on internal marks and attendance.

## Objectives

- Implement student result prediction using Python.
- Write automated unit tests using Python's `unittest` framework.
- Configure GitHub Actions to run tests automatically on every push to the `main` branch.
- Demonstrate an intentional test failure and fix it.

## Project Structure

- `result_logic.py` — Contains the student result prediction logic.
- `test_result_logic.py` — Contains automated unit tests.
- `.github/workflows/ci.yml` — Configures the GitHub Actions CI workflow.

## Result Prediction Rules

A student is classified as **PASS** when both conditions are satisfied:

- Internal marks are greater than or equal to 40.
- Attendance is greater than or equal to 75%.

Otherwise, the result is **FAIL**.

## Automated Testing

The project includes five unit tests:

1. Student passes with sufficient marks and attendance.
2. Student fails due to low internal marks.
3. Student fails due to low attendance.
4. Student fails when both conditions are insufficient.
5. Student passes at the minimum required marks and attendance.

## Continuous Integration Workflow

GitHub Actions automatically:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Executes the unit tests.
4. Reports whether the tests pass or fail.

The workflow runs on pushes to `main` and pull requests targeting `main`.

## Failure Demonstration

An intentional test failure was introduced by changing the expected result from `PASS` to `FAIL`. The workflow detected the incorrect expectation. The test was then restored to its correct value, and the workflow passed successfully.

## Technologies Used

- Python 3.11
- Python `unittest`
- GitHub Actions
- YAML

## Conclusion

This practical demonstrates how automated testing and GitHub Actions help identify errors early and verify Python code whenever changes are pushed to the repository.

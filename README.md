# Demographic Data Analyzer

This project is part of the freeCodeCamp Data Analysis certification. It uses the 1994 U.S. Census database (Adult Dataset) to explore and answer various demographic questions using Python and Pandas. The goal was to perform data wrangling, cleaning, and aggregation while validating each result with automated unit tests. A Jupyter Notebook was also used to explore and verify each analytical step.

## Table of Contents

- [Demographic Data Analyzer](#demographic-data-analyzer)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Screenshot](#screenshot)
  - [Dataset Description](#dataset-description)
  - [Questions Answered](#questions-answered)
  - [How to Run](#how-to-run)
    - [Locally](#locally)
  - [Notebook Exploration](#notebook-exploration)
  - [Testing](#testing)
  - [What I Learned](#what-i-learned)
  - [Author](#author)
  - [Acknowledgments](#acknowledgments)

## Overview

The project analyzes census data to answer questions such as:
- What is the average age of men?
- Which country has the highest percentage of rich people?
- What percentage of people with advanced degrees earn more than 50K?

All computations were done using Pandas, and verified using the built-in `unittest` framework. The final implementation passes all 10 tests provided by the starter code.

### Screenshot

A sample from the exploratory notebook showing initial calculations:

![Screenshot of analysis in Jupyter](./screenshot.png)

## Dataset Description

The dataset comes from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/20/adult) and contains over 32,000 entries with the following features:
- `age`, `workclass`, `education`, `marital-status`, `occupation`
- `race`, `sex`, `hours-per-week`, `native-country`, `salary`

Each row represents a person from the 1994 U.S. Census. Example:

| age | education | hours-per-week | race  | sex    | salary |
|-----|-----------|----------------|-------|--------|--------|
| 39  | Bachelors | 40             | White | Male   | <=50K  |
| 50  | Bachelors | 13             | White | Male   | <=50K  |
| 28  | Bachelors | 40             | Black | Female | <=50K  |

## Questions Answered

The project answers the following questions:

1. How many people of each race are represented in this dataset?
2. What is the average age of men?
3. What is the percentage of people who have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8. What country has the highest percentage of people that earn >50K?
9. What is that percentage?
10. What is the most popular occupation for those who earn >50K in India?

## How to Run

### Locally

Make sure you have Python ≥3.8 and `pip` installed. Then:

1. Clone the repository:
```bash
git clone https://github.com/your-username/demographic-data-analyzer.git
cd demographic-data-analyzer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run the analysis:
```bash
python main.py
```

This will output all results and optionally run unit tests (if enabled).

## Notebook Exploration

An optional Jupyter Notebook (exploration.ipynb) was used for:
- Step-by-step testing of logic and filters
- Verifying calculations against visual outputs
- Comparing intermediate statistics before implementing final code

To launch the notebook:
```bash
jupyter notebook
```

Then open exploration.ipynb in your browser.

## Testing

All logic is verified with automated tests using Python's unittest module.

To run all tests:
```bash
python main.py
```

or manually:
```bash
python -m unittest test_module.py
```

Each test corresponds to one of the questions in the prompt and ensures expected values match calculated results.

## What I Learned

Through this project, I gained hands-on experience with:
- Real-world data analysis using Pandas
- Boolean filtering, group-by aggregation, and Series/Index logic
- Writing readable, testable code under clear specifications
- Using Jupyter Notebooks for incremental problem solving
- Structuring a Python project with unit testing and CLI execution

## Author

- GitHub - [@dantvi](https://github.com/dantvi)
- LinkedIn - [@danieltving](https://linkedin.com/in/danieltving)

## Acknowledgments

- [freeCodeCamp](https://www.freecodecamp.org/) – for the dataset and project template
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/) – for the Adult dataset
- [Python Docs](https://docs.python.org/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- Stack Overflow and open source communities for always having a relevant thread
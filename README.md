# coffee-roulette

A web app (Python with Flask, and Angular) to pair people for coffee roulette. If there are an odd number of people to pair, one group of three is created.

## Getting started locally

Prerequisites: 
- Python 3.6 or higher
- Node.js 11 or higher
  
Running the backend:
1. In the `backend` directory, run `pip install -r requirements.txt` to install the required Python packages

Running the frontend:
1. Run `npm i` in the `frontend` directory to install dependencies
2. Install the Angular CLI globally: `npm install -g @angular/cli@latest`
2. Run `ng s` in the `frontend/` directory to run the frontend

## What is coffee roulette?

Every so often (e.g. once a month), people who have signed up are randomly paired with someone else. This is used in workplaces to provide employees with opportunities
to meet others in the firm (or department if the firm is large), some of whom they may not have otherwise had the chance to meet (e.g. due to different seniority 
or if your work does not overlap). 

(Meeting up for coffee serves as an excuse for getting to know someone -- actually drinking coffee is optional!)

## TODO:

- [ ] Export pairings into a spreadsheet
- [ ] Add unit tests and CI
- [ ] Read existing data from a spreadsheet (take into account who has already been paired from previous sessions)

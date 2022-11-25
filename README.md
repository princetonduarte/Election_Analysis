# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
	- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
	- Diana DeGette, who received 73.8% of the vote and 272.892 number of votes.

## Challenge Overview
The election commission has requested some additional data to complete the audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Challenge Summary
I needed to download the starter code which included the initial code that performed the analysis for each of the candidates. The challenge was to find the voter turnout for each county, percentage, and the highest turnout. 

### 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
### 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter_turnout = 0
winning_county_percentage = 0
### 3: Extract the county name from each row.
   county_name = row[1]
### 4a: Write an if statement that checks that the county does not match any existing county in the county list.
    if county_name not in county_options:
### 4b: Add the existing county to the list of counties.
      county_options.append(county_name)
### 4c: Begin tracking the county's vote count.
      county_votes[county_name] = 0
### 5: Add a vote to that county's vote count.
      county_votes[county_name] += 1


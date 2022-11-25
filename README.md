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

- The county votes were:
	- Jeferson county had 10.5% of the votes with 38,855 voters.
	- Denver county had 82.8% of the votes with 306,055 voters.
	- Arapahoe county had 6.7% of the votes with 24,801 voters.
- The highest county of voters that turned out was in Denver with nearly 83% of the 369,711 votes. 

### Election Analysis Text
![](https://github.com/princetonduarte/Election_Analysis/blob/1b52705638d75d1cfae05c755ed4e186d9509a5b/Resources/election_analysistxt.png)

### Terminal 
![](https://github.com/princetonduarte/Election_Analysis/blob/c061d5f62360505fbba1bcd78a906346844af7ad/Resources/terminal_election_results.png)

## The below code was added to [PyPoll_Challenge.py](https://github.com/princetonduarte/Election_Analysis/blob/664ad992e0909aad65d068c79fc5d1a867291193/PyPoll_Challenge.py).
#### 1: Create a county list and county votes dictionary.
	county_options = []
	county_votes = {}
#### 2: Track the largest county and county voter turnout.
	largest_county = ""
	county_voter_turnout = 0
winning_county_percentage = 0
#### 3: Extract the county name from each row.
   	county_name = row[1]
#### 4a: Write an if statement that checks that the county does not match any existing county in the county list.
    if county_name not in county_options:
#### 4b: Add the existing county to the list of counties.
      county_options.append(county_name)
#### 4c: Begin tracking the county's vote count.
      county_votes[county_name] = 0
#### 5: Add a vote to that county's vote count.
      county_votes[county_name] += 1
#### 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
#### 6b: Retrieve the county vote count.
        county = county_votes.get(county_name)
#### 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% {county:,}\n")

#### 6d: Print the county results to the terminal.
	print(county_results)
#### 6e: Save the county votes to a text file.
	txt_file.write(county_results)
#### 6f: Write an if statement to determine the winning county and get its vote count.
	if (county > county_voter_turnout) and (county_vote_percentage > winning_county_percentage):
		county_voter_turnout = county
        winning_county = county_name
         winning_county_percentage = county_vote_percentage
#### 7: Print the county with the largest turnout to the terminal.
    largest_county = (f"\n-------------------------\nLargest County Turnout: {winning_county}\n"
        "-------------------------\n")
    print(largest_county)
    txt_file.write(largest_county)    
#### 8: Save the county with the largest turnout to a text file.
	txt_file.write(largest_county) 

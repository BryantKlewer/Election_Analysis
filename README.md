# Election_Analysis

## Project Overview
* In this analysis we are tasked with auditing a recent Colorado Board of Elections local congressional election. In order to complete this audit, we were tasked with the following:
1. Tabulating the total number of votes cast in the election.
2. Populating a list of all the counties in the congressional precinct along with the total number of votes and percentage of total votes for each.
3. Determining which county had the largest number of votes in the election.
4. Populating a list of all candidates who received votes.
5. Calulating the total number of votes received by each candidate and the total percentage of votes won by each candidate.
6. Determining the winner of the election based on popular vote.

## Resources
* Data source: elction_analysis.csv
* Software: Python 3.10.4, Visual Studio Code 1.67.2

## Election Results
* After analyizing the election data the audit found that:
1. The total number of votes cast in the election was 369,711.
2. The individual county results were:
  - Jefferson County produced 38,855 total votes which accounted for 10.5% of the total votes that were cast.
  - Denver County produced 306,055 total votes which accounted for 82.8% of the total votes that were cast.
  - Arapahoe County produced 24,801 total votes which accounted for 6.7% of the total votes that were cast.
4. The county that produced the most votes in the election was:
  - Denver County which totaled 306,055 votes, or 82.8% of the total vote.
5. The candidates that recieved votes in the election were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
6. The individual candidate's election results were:
  - Charles Casper Stockham received 85,213 number of total votes which accounted for 23.0% of the total votes.
  - Diana DeGette received 272,892 number of total votes which accounted for 73.8% of the total votes.
  - Raymon Anthony Doane received 11,606 number of total votes which accounted for 3.1% of the total votes.
7. The winner of the election was:
  - Diana DeGette who received 272,892 of the total popular vote and 73.8% of the total votes.
8. Here is the summary below:
  - ![](https://github.com/BryantKlewer/Election_Analysis/blob/main/pics/analysis_output.png)

## Summary
* In summary, a script was written in order to determine all counties that participated in congressional election as well as their total number of votes and what percentage of votes those accounted for. Additionally, it found all candidates in the election and accumulated their total number of votes and what percentage they recieved. Finally, it output all of this information as well as which county produced the highest number of total votes and the winner of the election into a text document for ease of understanding. The creation of the the script used in this analysis is beneficial to the election commission into the future. This script can be modified to allow for other election analysis results to be produced. Simply determine what election information you would like to have summarized and change a couple of words in the script and out comes the new analysis. For example, this script could be used for any election in the state from the gubernatorial to a town council election. Lets take a look at how this could be done if we wanted to use this base script in order to determine who won the gubernatorial race. ![](https://github.com/BryantKlewer/Election_Analysis/blob/main/pics/screen_1.png) Looking at the screen shot above, we would first change our election input file as seen on line 9 and our output text document for the resulults on line 11. All of our candidate and winner information is already set to be tracked as is our county level data. We would be done at this point. If we were going to another variable such as neighborhoods for a town council election we change our list and dictionary names on lines 21 and 22 and our count varibles on 30 and 31. Next we would update our script with the new names and variables, lines 67 through 76, as well as extract the correct metric we want from the original input document as seen below on line 50. ![](https://github.com/BryantKlewer/Election_Analysis/blob/main/pics/screen_2.png) And finally, we would need to update our output to the text summary file. Again, we would update our list, dictionary, and variables as seen in lines 94 through 108. We additionally need to update the scipt on the txt file as seen on lines 110 through 114 below. ![](https://github.com/BryantKlewer/Election_Analysis/blob/main/pics/screen_3.png)





# Election_Analysis
## Overview of Election Audit
The reason for this Election Audit was to send some additional data as requested by the election commission.  They wanted more data to show the voter turnout for each county, the percentage of votes from each county out of the total votes, and the county with the highest turnout.  In order to do this, I had to add some code to a script that we had previously been working on in order to get the results wanted by the election commission.


The first thing I had to do was initialize some variables to hold the new values I was to work with.  I initialized a county list, a county votes dictionary, an empty string for largest_county_turnout, and then set largest_county_vote to zero.  Then I pulled the county name from each row to begin tracking the counties votes.  I then wrote an if statement to check if the county was in the list, if not, it was to be added to the list.  Then I set a county votes by county name variable to begin tracking the votes, and incremented that by 1.


In the section after the code to print the election results, I started a for loop to loop through the counties in order to get their total votes, and to calculate the percentages of votes per county.  Another if statement was added to find the winning county, which was then printed to the text file, and to the terminal.


By adding those things to the script, I was able to print out the results for total votes, total votes per county along with their percentages, and which county had the largest turnout.  This was added to the previously found candidate data.

## Election Audit Results
* The total amount of votes cast in the congressional election were 369,711
![Screenshot_20221207_093903](https://user-images.githubusercontent.com/45715246/206208241-81895bdc-0a05-4bbf-a76f-dea15a9cb582.png)
* Of the total 369,711 votes: Jefferson county provided 38,855 which was 10.5% of the total votes.  Denver county provided 306,055 votes which was the majority of the votes with 82.8%.  Arapahoe county posted 24,801 votes which was the lowest percentage with 6.7% of the total votes.
![Screenshot_20221207_095123](https://user-images.githubusercontent.com/45715246/206211322-21001959-4d29-4884-855e-f61a8b405f3d.png)

 ![Screenshot_20221207_094305](https://user-images.githubusercontent.com/45715246/206209777-fd4ad357-a589-468e-a0f3-7d56df903e8a.png)
* The county with the largest number of votes was Denver with 82.8% of the total votes.

![Screenshot_20221207_094805](https://user-images.githubusercontent.com/45715246/206210226-507d884f-ff1a-4acb-b1cc-e7628d29d1a4.png)

* Breakdown of the total votes and percentages of votes by candidate:
![Screenshot_20221207_095507](https://user-images.githubusercontent.com/45715246/206212099-a5ceaaa1-9c05-4d3e-b549-145d92b93ef4.png)

![image](https://user-images.githubusercontent.com/45715246/206211775-36f1f720-02b5-40f0-9347-cc25aa4d199b.png)
* The winning candidate was Diana DeGette with a total of 272,892 votes for a percentage of 73.8% of the total votes.
![image](https://user-images.githubusercontent.com/45715246/206212761-2fc9397a-709a-455d-81eb-02b7311b255e.png)

## Election Audit Summary
This script can be used in any congressinal precinct just by adding a new csv file with different voter precinct information.  You can use the code exactly the same, and it will print out the election results by county for any counties in the csv file.  This file can still be used even if there are a larger amount of counties, and candidates in the csv file.  Another way to modify this script to be used for other elections, is that you can also add additional code to find additional election results for other elected positions such as governor, mayor, judges, and any other elected official.  You can add a similar section of code as the winning congressional candidate with new variables to tally the votes for the other elected position.  

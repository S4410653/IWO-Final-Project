
# Introduction
In this GitHub repository you will find the following files: clean_data.py, Randstad_plaatsnamen.json, Niet-Randstad_plaatsnamen and iwo_Final_Project.ipynb.

All other files than these can be ignored. 

Randstad_plaatsnamen.json contains all the city names of the cities and villages of the Randstad.

Niet-Randstad_plaatsnamen.josn contains all the city names of the cities and villages not in the Randstad.

iwo_Final_Project.ipynb contains the code to search for the amount of occurrences of 'tractor' and 'trekker' in the separated text files and the contingency matrix.

clean_data.py inside the file you can find the explanation of the code.

# How to get the data
Log in on Karora and make a directory (mkdir <name_of_directory>).
## In Karora:
Extracting all tweets of 10-2019: <S_number>@karora:~/<name_of_directory>$ zless /net/corpora/twitter2/Tweets/2019/10/*.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location > tweets_10_2019.txt
Extracting all tweets of 02-2020: <S_number>@karora:~/<name_of_directory>$ zless /net/corpora/twitter2/Tweets/2020/02/*.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location > tweets_02_2020.txt
Extracting all tweets of 07-2020: <S_number>@karora:~/<name_of_directory>$ zless /net/corpora/twitter2/Tweets/2020/07/*.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location > tweets_07_2020.txt

## In Linux shell:
Copy to local server 10-2019: scp <S_number>@karora.let.rug.nl:<name_of_directory>/tweets_10_2019.txt <Enter here the path to where you want to save the file> (/mnt/c/Users/) 
Copy to local server 02-2020: scp <S_number>@karora.let.rug.nl:<name_of_directory>/tweets_02_2020.txt <Enter here the path to where you want to save the file> (/mnt/c/Users/) 
Copy to local server 07-2020: scp <S_number>@karora.let.rug.nl:<name_of_directory>/tweets_07_2020.txt <Enter here the path to where you want to save the file> (/mnt/c/Users/) 

## If you want to control if the extraction went well:
In Linux shell (the path of the terminal has to lead to the same folder where the textfiles are located):
Compare cat tweets_10_2019.txt | tail with <S_number>@karora:/net/corpora/twitter2/Tweets/2019/10$ zless /net/corpora/twitter2/Tweets/2019/10/20191031\:23.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location | tail
Compare cat tweets_02_2020.txt | tail with <S_number>@karora:/net/corpora/twitter2/Tweets/2020/02$ zless /net/corpora/twitter2/Tweets/2020/02/20200229\:23.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location | tail
Compare cat tweets_07_2020.txt | tail with <S_number>@karora:/net/corpora/twitter2/Tweets/2020/07$ zless /net/corpora/twitter2/Tweets/2020/07/20200731\:23.out.gz | /net/corpora/twitter2/tools/tweet2tab -i text user.location | tail

# steps to follow before executing clean_data.py
## Installations:
Install of text-preprocessing: (python 3.7 and 3.8)
				  pip3 install text-preprocessing
Install of jupyter:
				  pip3 install notebook 
				  
NOTE: text-preprocessing library is used, we know certain it works in python 3.7 and 3.8, but for later versions is unknown to us (the current development status is 2 - Pre-Alpha).
				  
# Command lines to run
python3 clean_data.py tweets_10_2019.txt Randstad_plaatsnamen.json Niet-Randstad_plaatsnamen.json
python3 clean_data.py tweets_02_2020.txt Randstad_plaatsnamen.json Niet-Randstad_plaatsnamen.json
python3 clean_data.py tweets_07_2020.txt Randstad_plaatsnamen.json Niet-Randstad_plaatsnamen.json

# Steps to follow after executing clean_data.py
Converting text file(.txt) to comma separated file(.csv) in the terminal (the path of the terminal has to lead to the same folder where the textfiles are located):
cat all_tweets_RS.txt | tr -s '\t' ',' > all_tweets_RS2.txt
cat all_tweets_not_RS.txt | tr -s '\t' ',' > all_tweets_not_RS2.txt

NOTE: the code uses an append method to concatenate the files, so if something goes wrong during running the code start all over(delete the created files).

## Inserting column titel:
Open all_tweets_RS2 in a text editor -> make sure the flickering '|' is on the far left side of line 1 -> press enter and go back to line 1 (far left) -> type 'Tweets,Locatie' (without the '') -> save the file
Open all_tweets_not_RS2 in a text editor-> make sure the flickering '|' is on the far left side of line 1 -> press enter and go back to line 1 (far left) -> type 'Tweets,Locatie' (without the '') -> save the file

# Code used to show results
## In the Linux shell:
Run jupyter notebook -> copy the link/URL that starts with 'https://localhost' -> paste this link in the browser and click on enter (step 2 and 3 can be skipped if jupyter is already opened in the browser) -> \
click on 'iwo_Final_Project.ipynb' -> in the navigation bar, click on 'Cell' and click on 'Run All'.


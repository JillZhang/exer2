Step 1:
Please go to the /exer2/src/sprouts/tweets.py and edit the tweet credentials, which should have four entries:
Consumer_key
Consumer_secret
Assess_token
Access_token_secret
twitter_credentials = {
    "consumer_key"        :  "<enter your consumer key>",
    "consumer_secret"     :  "<enter your consumer secret key>",
    "access_token"        :  "<enter your access token>",
    "access_token_secret" :  "<enter your access token secret key>",
}

Step 2:
Create the database “tcount” and create the table “tweetcount” in postgres by run the script create_table.py
Step 3:
Please cd to the extweetwordcount folder. Then enter “Sparse run”. The application will start to collect tweets.
Step 4:
Press Control+C when you want to stop the collecting. All the data will be loaded into the tweetwordcount table. You can use the psycopg2 to access the data.

Two scripts have been written up:
Script1: finalresults.py: please cd to the extweetwordcount folder. Enter “python finalresults.py <any single word you want to query>”.
Script2: histogram.py:  please cd to extweetwordcount folder. Enter “python histogram.py <k1> <k2>”. It will return the histogram words counts within the specified counts.


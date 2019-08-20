# Project Summary

### Background
This project is to help a startup called **Sparkify** to understand what songs users are listening to. Sparkify has been collecting on songs and user activity on their new music streaming app. 
As their use base and song data have grown even more, they decide to move their data warehouse to a **data lake**.


### Datasets
Two datasets that reside in S3(AWS simple storage service):

1.**Song Dataset**
    > Each file is in JSON format and contains metadata about a song and the artist of that song. <br>
    > File names are like 'song_data/A/B/C/TRABCEI128F424C983.json' etc. <br>
    > In each file, data are like: {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
2.**Log Dataset**
    > Each file is in JSON format and contains logs on user activity on the app <br>
    > File names are like 'log_data/2018/11/2018-11-12-events.json' etc. <br>
    > below is an example of what the data in a log file, 2018-11-12-events.json, looks like

![](screenshots/log-data.png)
    

### Tasks
1.**Extract data from _S3_**
    > extract song data from S3<br>
    > extract log data from S3<br>
2.**Process data into analytics tables using _Spark_**
    > fact table: songplays<br>
    > dimension tables: users, songs, artists, time<br>
3.**Load data back into _S3_>**
    > data stored in parquet files


# To run the Python scripts
1.Get _Access Key_ from IAM_USERS to fill dl.cfg file
2.Click _File -> New -> Console_ at top menu
3.Select kernel _Python3_
4.Type `%run etl.py` in the console cell
5.Click _Run -> Run selected cell_ at top menu

        
---
# Files in the repository
The project workspace includes three files:
- **_etl.py_** reads data from S3, processes that data using Spark, and writes them back to S3.
- **_dl.cfg_** contains AWS credentials.
- **_README.md_** provides discussion on the project.
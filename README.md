# Project Summary

### Background
This project is to help a startup called **Sparkify** to understand <br>
what songs users are listening to. Sparkify has been collecting on <br>
songs and user activity on their new music streaming app. As their <br>
use base and song data have grown even more, they decide to move <br>
their data warehouse to a **data lake**.


### Datasets
Two datasets that reside in S3(AWS simple storage service):

1. **Song Dataset**<br>
    - Each file is in JSON format and contains metadata about a song <br>
    and the artist of that song. <br>
    - File names are like 'song_data/A/B/C/TRABCEI128F424C983.json' etc. <br>
    - In each file, data are like: <br>
    {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, <br>
    "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", <br> 
    "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", <br>
    "duration": 152.92036, "year": 0}<br>
2. **Log Dataset**<br>
    - Each file is in JSON format and contains logs on user activity on the app <br>
    - File names are like 'log_data/2018/11/2018-11-12-events.json' etc. <br>
    

### Tasks
1. **Extract data from _S3_**<br>
    - extract song data from S3<br>
    - extract log data from S3<br>
2. **Process data into analytics tables using _Spark_**<br>
    - fact table: songplays<br>
    - dimension tables: users, songs, artists, time<br>
3. **Load data back into _S3_**<br>
    - data stored in parquet files<br>

---
# To run the Python scripts
1. Get _Access Key_ from IAM_USERS to fill dl.cfg file<br>
2. Click _File -> New -> Console_ at top menu<br>
3. Select kernel _Python3_<br>
4. Type `%run etl.py` in the console cell<br>
5. Click _Run -> Run selected cell_ at top menu<br>
        
---
# Files in the repository
The project workspace includes three files:
- **_etl.py_** reads data from S3, processes that data using Spark,<br>
and writes them back to S3.
- **_dl.cfg_** contains AWS credentials.
- **_README.md_** provides discussion on the project.

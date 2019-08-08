import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.functions import monotonically_increasing_id

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = "s3a://udacity-dend/song_data/*/*/*/*.json"

    # read song data file
    df_song = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table =
    df_song.select("song_id", "title", "artist_id", "year", "duration")
    .dropDuplicates()

    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year", "artist_id")
    .format("parquet").save("s3a://udacity-dend/songs")

    # extract columns to create artists table
    artists_table =
    df_song.select(
        "artist_id", col("artist_name").alias("name"),
        col("artist_location").alias("location"),
        col("artist_latitude").alias("latitude"),
        col("artist_longitude").alias("longitude"))
    .dropDuplicates()

    # write artists table to parquet files
    artists_table.write.format("parquet").save("s3a://udacity-dend/artists")


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = "s3a://udacity-dend/log_data/*/*/*.json"

    # read log data file
    df_log = spark.read.json(log_data)

    # filter by actions for song plays
    df_log = df_log.where(df_log.page == "NextSong")

    # extract columns for users table
    users_table =
    df_log.select(
        col("userId").alias("user_id"),
        col("firstName").alias("first_name"),
        col("lastName").alias("last_name"),
        "gender", "level")
    .dropDuplicates()

    # write users table to parquet files
    users_table.write.format("parquet").save("s3a://udacity-dend/users")

    # create timestamp column from original timestamp column
    get_timestamp =
    udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))
    df_log = df_log.withColumn("timestamp", get_timestamp(df_log.ts))

    # create datetime column from original timestamp column
    get_datetime =
    udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d'))
    df_log = df_log.withColumn("datetime", get_datetime(df_log.ts))

    # extract columns to create time table
    time_table =
    df_log.select(
        df_log.timestamp.alias('start_time'),
        hour(df_log.datetime).alias('hour'),
        dayofmonth(df_log.datetime).alias('day'),
        weekofyear(df_log.datetime).alias('week'),
        month(df_log.datetime).alias('month'),
        year(df_log.datetime).alias('year'),
        date_format(df_log.datetime, 'u').alias('weekday'))
    .dropDuplicates()

    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year", "month").
    format("parquet").save("s3a://udacity-dend/time")

    # read in song data to use for songplays table
    song_df = log_song

    # extract columns from joined song and log datasets to create songplays table
    cond = [df_song.title == df_log.song, df_song.artist_name == df_log.artist]
    df = df_log.join(df_song, cond, 'outer')
    .withColumn("songplay_id", monotonically_increasing_id())
    songplays_table =
    df.select(
        df.songplay_id, df.timestamp.alias('start_time'),
        df.userId.alias('user_id'), df.level,
        df.song_id, df.artist_id, df.sessionId.alias('session_Id'),
        df.location, df.userAgent.alias('user_agent'),
        year(df.datetime).alias('year'), month(df.datetime).alias('month'))

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year", "month")
    .format("parquet").save("s3a://udacity-dend/songplays")


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://udacity-dend/"

    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()

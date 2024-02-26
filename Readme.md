# Beam Stream Bikesharing
This Python script uses Apache Beam to create a data pipeline that reads data from a Pub/Sub topic, transforms it, and writes it to a BigQuery table.

## How it works:

The script sets up a Beam pipeline with streaming enabled. It reads data from a specified Pub/Sub subscription, decodes the data from UTF-8, parses the JSON, and writes the resulting data to a BigQuery table.

The Pub/Sub subscription and BigQuery table are specified by the `INPUT_SUBSCRIPTION` and `OUTPUT_TABLE` variables, respectively.

The schema for the BigQuery table is defined in the `WriteToBigQuery` step of the pipeline.

## Running the script
To run the script, simply execute the `beam_stream_bikesharing.py` file. The script will automatically start processing data from the Pub/Sub subscription and writing it to the BigQuery table.

Please ensure that you have the necessary permissions to read from the Pub/Sub subscription and write to the BigQuery table.
import apache_beam as beam
import argparse
import json
import logging

from apache_beam.options.pipeline_options import PipelineOptions

INPUT_SUBSCRIPTION= 'projects/resounding-hope-414923/subscriptions/bike-sharing-trips-subs-felipe'
OUTPUT_TABLE = 'resounding-hope-414923:raw_bikesharing_felipe.bike_trips_streaming_felipe'

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
beam_options = PipelineOptions(beam_args, streaming=True)

def run():
    with beam.Pipeline(options=beam_options) as p:(
        p | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(subscription=INPUT_SUBSCRIPTION)
        | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
        | "Parse JSON" >> beam.Map(json.loads)
        | 'Write to Table' >> beam.io.WriteToBigQuery(OUTPUT_TABLE,
                        schema='trip_id:STRING,start_date:TIMESTAMP,start_station_id:STRING,bike_number:STRING,duration_sec:INTEGER',
                        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
    )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
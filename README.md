# Migration tTols
This tool can help you measure the following data on a Datadog account:

* Which metrics the prospect is sending to his Datadog account

* How many metrics per each metric

* Interval collection for each metric

* Total DPM

## Getting Started:

1. Install Datadog api:

   `pip install datadog`

2. Ask the customer to get the Api token and Application token from his [Datadog UI](https://app.datadoghq.com/account/settings#api)

3. Run the script and wait

    `python datadog_metrics_count.py`
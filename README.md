# Async Job Queueing System
This is the project that uses the concepts of Advanced Python and here they are, advanced project showing mastering of concepts of python, project structuring and simulating how job queueing systems works under the hood which gives better understanding
## Python Concepts
- Context Management (resource | session management)
- Decorators (@retry, @log, @timeit)
- Generators (streaming task)
- DB (sqlite3)
- Async I/O

## Core Concepts
- Producers
- Consumers
- Task | Job Queue

![Producer, Message Queue, Consumer diagram](https://substackcdn.com/image/fetch/$s_!pfuM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfddd2c7-016f-40f3-8a13-f38748ccbddb_1104x378.png)

## Project Structure
```
async_job_queue/
│
├── job_queue/
│   ├── __init__.py
│   ├── producer.py         # submit_job(), bulk_insert_jobs()
│   ├── consumer.py         # async run_worker()
│   ├── decorators.py       # @retry, @log, @timeit
│   ├── context.py          # DBSessionManager (context manager)
│   ├── storage.py          # DB ops (insert, fetch, update)
│   ├── jobs.py             # actual job functions
│   ├── job_gen.py          # generator for queued jobs
│
├── db/
│   └── schema.sql
│
├── scripts/
│   ├── start_worker.py     # Starts the consumer loop
│   ├── submit_jobs.py      # Adds new jobs to queue
│
├── logs/
│   └── jobs.log
│
├── tests/
│   └── test_jobs.py
│
├── .env
├── config.py
├── README.md
└── requirements.txt
```
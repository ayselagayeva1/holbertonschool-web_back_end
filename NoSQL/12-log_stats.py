#!/usr/bin/env python3
"""
12-log_stats.py
Provide some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def main():
    """
    Connects to MongoDB 'logs' database, fetches statistics from
    the 'nginx' collection and prints:
      - total number of logs
      - number of logs per HTTP method (GET, POST, PUT, PATCH, DELETE)
      - number of GET requests to the '/status' path
    """
    client = MongoClient()  # localhost:27017
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Number of documents per method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()

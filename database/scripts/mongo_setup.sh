#!/bin/bash
echo "sleeping for 10 seconds"
sleep 10

echo mongo_config.sh time now: `date +"%T" `
mongo --host mongo0:27017 <<EOF
  var cfg = {
    "_id": "rs0",
    "version": 1,
    "members": [
      {
        "_id": 0,
        "host": "mongo0:27017",
        "priority": 2
      },
      {
        "_id": 1,
        "host": "mongo1:27017",
        "priority": 0
      },
      {
        "_id": 2,
        "host": "mongo2:27017",
        "priority": 0
      }
    ]
  };
  rs.initiate(cfg);
EOF
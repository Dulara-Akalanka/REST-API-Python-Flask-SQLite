from flask import Flask, request, jsonify
import json
import sqlite3


app = Flask(__name__)


def db_connection():
   conn = None
   try:
       conn = sqlite3.connect("events.sqlite")
   except sqlite3.error as e:
       print(e)
   return conn




events_list = [
   {
       "id":0,
       "event_type": "pull_request",
       "event_name": "change_event"
   },


   {
       "id":1,
       "event_type":"release",
       "event_name":"deployment_event"
   },
   {
       "id":2,
       "event_type":"push",
       "event_name":"workflow_event"
   },
   {
       "id":3,
       "event_type": "pull_request_merged",
       "event_name":"deployment_event"
   }
]
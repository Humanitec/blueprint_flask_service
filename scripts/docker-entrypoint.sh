#!/bin/bash

# TODO: run migrations here

gunicorn  app.wsgi:app --config gunicorn_conf.py
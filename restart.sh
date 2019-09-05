#!/usr/bin/env bash
pkill gunicorn
gunicorn config.wsgi:application -b 0.0.0.0:8001 --daemon -t 300
#!/bin/sh -e

uvicorn app.main:app ${@}

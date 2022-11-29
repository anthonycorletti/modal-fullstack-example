#!/bin/sh -ex

mypy app tests
black app tests --check
isort app tests scripts --check-only
ruff app tests scripts

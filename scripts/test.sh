#!/bin/sh -ex

./scripts/lint.sh

pytest --cov=app --cov=tests --cov-report=term-missing --cov-report=xml -o console_output_style=progress --disable-warnings ${@}

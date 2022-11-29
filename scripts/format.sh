#!/bin/sh -ex

black app tests scripts
isort app tests scripts
ruff app tests scripts --fix

# Gamified Portal

Developed in Python and Flask

## Overview

This portal displays tasks, (optional) supplementals, bank account information,
and buttons which allow users to signal for 'help' or that they are 'finished'
with a task.

Each user begins at level '1' and will initially not receive a task.
User level ids dictate which task is to be delivered.
Tasks are configured in '/app/main/views.py'

## Details
To run locally, set an environmental variable for the secrect key (bash syntax):
`export SECRET_KEY="mysekritvalue"`
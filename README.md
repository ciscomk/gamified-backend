_this project has been deprecated. the current version of this project can be found here: https://github.com/ciscomk/funandprofitlabs_portal_

# Gamified Portal

Developed in Python and Flask

## Overview

This portal displays tasks, (optional) supplementals, bank account information,
and buttons which allow users to signal for 'help' or that they are 'finished'
with a task.

Each user begins at level '1' and will not receive a task.
User level ids dictate which task is to be delivered.
Tasks & Supplements are configured in '/app/main/views.py'
Tasks & Supplements are added in 'app/templates' as .html files.
This repo does not contain any tasks.

## Details
To run locally, set an environmental variable for the secrect key.
For example (bash syntax): `export SECRET_KEY="mysekritvalue"`

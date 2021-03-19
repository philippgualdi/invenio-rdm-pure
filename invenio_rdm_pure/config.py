# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Technische Universität Graz.
#
# invenio-rdm-pure is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds pure."""

# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

from celery.schedules import crontab

INVENIO_RDM_PURE_DEFAULT_VALUE = "foobar"
"""Default value for the application."""

INVENIO_RDM_PURE_BASE_TEMPLATE = "invenio_rdm_pure/base.html"
"""Default base template for the demo page."""

CELERYBEAT_SCHEDULE = {
    "synchronize_records": {
        "task": "invenio_rdm_pure.tasks.synchronize_records",
        "schedule": crontab(hour=1, minute=0, day_of_week=0),
    },
}


# Invenio-RDM-Pure
INVENIO_PURE_CONFIG_PRESENT = False
"""Helper variable to check the presence of pure configuration.

   If the values are present and correct in invenio.cfg
   this variable should be set to True.
   """

# Invenio
INVENIO_PURE_HOST_URL = "https://127.0.0.1:5000/"
"""URL of invenio host."""

INVENIO_PURE_RECORD_URL = INVENIO_PURE_HOST_URL + "api/records/{}"
"""Endpoint to access single a record."""

INVENIO_PURE_RECORDS_URL = INVENIO_PURE_HOST_URL + "api/records"
"""Endpoint to access multiple records."""

INVENIO_PURE_USER_EMAIL = ""
"""Email of user creating the records."""

INVENIO_PURE_USER_PASSWORD = ""
"""Password of user creating the records."""


# Pure
PURE_API_URL = ""
"""URL of the Pure Instance's REST API."""

PURE_API_KEY = ""
"""Token/Key of the Pure Instance's REST API."""

PURE_USERNAME = ""
"""Username of Pure user having the necessary permissions to acquire needed Pure entries."""

PURE_PASSWORD = ""
"""Password of Pure user having the necessary permissions to acquire needed Pure entries."""

PURE_RESPONSIBLE_EMAIL = ""
"""Email address of Pure user having the necessary permissions to delete Pure entries."""

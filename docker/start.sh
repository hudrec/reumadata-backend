#!/usr/bin/env bash
MANAGE_PARAM=""

if [ -z "$APP_ENV" ]; then
    MANAGE_PARAM="--settings=reumadata_backend.settings.local"
else
    if [ "$APP_ENV" = "DEV" ]; then
        MANAGE_PARAM='--settings=reumadata_backend.settings.dev'
    elif [ "$APP_ENV" = "PROD" ]; then
        MANAGE_PARAM='--settings=reumadata_backend.settings.prod'
    fi
fi


cd reumadata_backend
poetry run python manage.py migrate $MANAGE_PARAM
poetry run python manage.py collectstatic --no-input $MANAGE_PARAM
poetry run python manage.py runserver 0.0.0.0:8000 $MANAGE_PARAM


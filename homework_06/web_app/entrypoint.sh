#!/bin/bash

echo "Starting.........."
echo "Preforming migrations..."
flask db upgrade
echo "Migrations done!"
exec "$@"

#!/bin/bash
echo "Cleaning up..."
docker-compose down
docker system prune -f
rm -rf venv

echo "running pycodestyle..."; pipenv run pycodestyle .; echo "running pydocstyle..."; pipenv run pydocstyle .
echo "running pytest..."
pipenv run pytest .
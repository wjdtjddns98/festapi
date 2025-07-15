set -eo pipefail

COLOR_GREEN=`tput setaf 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "black 실행"
poetry run black .
echo "OK"

echo "ruff 실행"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "OK"

echo "Mypy 실행"
poetry run dmypy run -- .
echo "OK"

echo "커버리지 체크"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html

echo "${COLOR_GREEN}성공띠${COLOR_NC}"

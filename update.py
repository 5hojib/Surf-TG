from os import path, getenv
from logging import FileHandler, StreamHandler, INFO, basicConfig, error, info
from logging.handlers import RotatingFileHandler
from subprocess import run
from dotenv import load_dotenv

basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=50000000, backupCount=10),
        StreamHandler(),
    ],
)
load_dotenv('config.env', override=True)

UPSTREAM_REPO = getenv('UPSTREAM_REPO', "https://github.com/5hojib/Surf-TG")
UPSTREAM_BRANCH = getenv('UPSTREAM_BRANCH', "main")

if UPSTREAM_REPO is not None:
    if path.exists('.git'):
        run(["rm", "-rf", ".git"])
        
    update = run([f"git init -q \
                     && git config --global user.email yesiamshojib@gmail.com \
                     && git config --global user.name 5hojib \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')

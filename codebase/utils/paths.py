from pathlib import Path

#current directory
BASE_DIR = Path.cwd()

#go one level up 
#PROJECT_DIR = BASE_DIR.parent 

#input dir
INPUT_DIR = BASE_DIR / 'data' / 'input'

#output dir
OUTPUT_DIR = BASE_DIR / 'data' / 'output'

#log error message
LOG_ERROR = BASE_DIR

#define the path of the log file
log_error_txt = rf'{LOG_ERROR}\error_log.txt'
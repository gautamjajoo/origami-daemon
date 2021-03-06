WELCOME_TEXT = """\
\t                           Origami Daemon
\t                    ----------------------------
\t This utility is used to deploy and manage demos on CloudCV servers.
\t To view all the commands available use --help flag

\t                          @CloudCV Origami

\t                    x--------------------------x
"""

ORIGAMI_CONFIG_DIR = '.origami'
ORIGAMI_DEMOS_DIRNAME = 'demos'

DEFAULT_API_SERVER_PORT = 9002

LOGS_DIR = 'logs'
ORIGAMI_STATIC_DIR = 'static'
ORIGAMI_DEPLOY_LOGS_DIR = 'deploy/logs/'
LOGS_FILE_MODE_REQ = 'w+'
DEFAULT_LOG_FILE = 'origami.log'

REQUIREMENTS_FILE = 'requirements.txt'
ENTRYPOINT_PYTHON_MODULE = 'main.py'
DOCKERFILE_FILE = 'Dockerfile'

BUNDLE_ZIP_MAX_COMPRESSED_SIZE = 500 * 1000 * 1000  # 500 MB
BUNDLE_ZIP_MAX_UNCOMPRESSED_SIZE = 1000 * 1000 * 1000  # 1000 MB

ORIGAMI_ENV_FILE = 'origami.env'

ORIGAMI_DB_NAME = 'origami.db'

DOCKER_UNIX_SOCKET = 'unix://var/run/docker.sock'

DEMOS_PORT_COUNT_START = 20001
DEMOS_PORT_COUNT_END = 30000

ORIGAMI_WRAPPED_DEMO_PORT = 9001

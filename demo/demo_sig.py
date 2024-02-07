from os import getpid
pid = getpid()
print('Running with pid: ', pid)

from os import kill
from signal import SIGKILL
kill(pid, SIGKILL)
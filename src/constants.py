from models import Cwd, ExecVe, Path, ProcTitle, SysCall

LOG_GLOB_PATTERN = r"src/logs/auditd.log*"  # Obviously pattern should be /var/log/audit/auditd.log*
DATABASE = "auditd.sqlite"
MESSAGE_CLS_MAPPING = {
    "CWD": Cwd,
    "EXECVE": ExecVe,
    "SYSCALL": SysCall,
    "PROCTITLE": ProcTitle,
    "PATH": Path,
}

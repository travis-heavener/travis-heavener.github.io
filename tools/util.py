from datetime import datetime
import re

def gen_timestamp(include_top_anchor: bool) -> str:
    return f"<p>Updated {datetime.now().strftime('%b. %Y')}{' &emsp; &emsp; <a href=\"#\">Back to Top</a>' if include_top_anchor else ''}</p>"

def gen_timestamp_txt() -> str:
    return f"Updated {datetime.now().strftime('%b. %Y')}"

def indent(n: int) -> str:
    return " " * (4 * n)

def pad_left(s: str, max_len: int) -> str:
    if len(s) >= max_len: return s
    return " " * (max_len - len(s)) + s

def pad_right(s: str, max_len: int) -> str:
    if len(s) >= max_len: return s
    return s + (" " * (max_len - len(s)))

###############################################

SHELL_COLORS = {
    "%A": "\033[0m",
    "%B": "\033[1m",
    "%C": "\033[3m",
    "%D": "\033[4m",
    "%E": "\033[38;5;8m",
    "%F": "\033[38;2;155;0;0m",
    "%G": "\033[38;2;175;0;0m",
    "%H": "\033[38;2;195;0;0m",
    "%I": "\033[38;2;215;0;0m",
    "%J": "\033[38;2;235;0;0m",
    "%K": "\033[38;2;255;0;0m",
    "%L": "\033[38;5;172m",
    "%M": "\033[38;5;187m",
    "%N": "\033[38;2;110;155;245m",
    "%O": "\033[38;5;214m",
    "%P": "\033[93m",
    "%Q": "\033[38;5;78m",
    "%R": "\033[38;2;160;205;255m",
    "%S": "\033[38;2;210;225;255m",
    "%T": "\033[38;2;255;155;70m",
    "%U": "\033[38;2;235;235;30m",
    "%V": "\033[38;2;230;155;240m"
}

def escape_shell_colors(body: str) -> str:
    for k, v in SHELL_COLORS.items():
        body = re.sub(rf"(?<!%){k}", v, body)
    return body
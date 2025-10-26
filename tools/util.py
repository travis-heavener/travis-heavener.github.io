from datetime import datetime

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
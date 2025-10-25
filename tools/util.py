from datetime import datetime

def gen_timestamp(include_top_anchor: bool) -> str:
    return f"<p>Updated {datetime.now().strftime('%b. %Y')}{' &emsp; &emsp; <a href=\"#\">Back to Top</a>' if include_top_anchor else ''}</p>"
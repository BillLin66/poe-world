import os
from typing import Any, Optional


def with_data_root(config: Optional[Any], path: str = '') -> str:
    data_root = '.' if config is None else str(getattr(config, 'data_root', '.'))
    return data_root if path == '' else os.path.join(data_root, path)

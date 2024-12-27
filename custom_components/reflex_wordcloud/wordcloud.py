"""Reflex custom component Wordcloud."""

import reflex as rx
from reflex.components.component import NoSSRComponent
from typing import List, Dict, Any, Tuple, Optional


class Wordcloud(NoSSRComponent):
    """Wordcloud component."""

    library = "react-wordcloud"

    tag = "ReactWordcloud"

    is_default = True

    words: rx.Var[List[Dict[str, str | int]]] = []

    max_words: rx.Var[int] = 100

    options: rx.Var[Dict[str, Any]] = {}

    size: Optional[Tuple[int, int]] = None

    min_size: Optional[Tuple[int, int]] = None


wordcloud = Wordcloud.create

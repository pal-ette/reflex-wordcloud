"""Reflex custom component Wordcloud."""

import reflex as rx
from reflex.components.component import NoSSRComponent
from typing import List, Dict, Any, Tuple


class Wordcloud(NoSSRComponent):
    """Wordcloud component."""

    library = "react-wordcloud"

    tag = "ReactWordcloud"

    is_default = True

    words: rx.Var[List[Dict[str, str | int]]] = []

    options: rx.Var[Dict[str, Any]] = {}

    size: rx.Var[Tuple[int, int]] = (600, 400)

    min_size: rx.Var[Tuple[int, int]] = (300, 300)


wordcloud = Wordcloud.create

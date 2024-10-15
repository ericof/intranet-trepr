from trepr.intranet import logger
from trepr.intranet.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent


def _update_excluded_from_nav(obj: Area):
    """Atualiza exclude_from_nav para conteúdo do tipo Área."""
    description = obj.description
    obj.exclude_from_nav = False if description else True
    logger.info(f"Atualiza o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    # Altera exclude_from_nav
    _update_excluded_from_nav(obj)

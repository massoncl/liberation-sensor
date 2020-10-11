# The domain of your component. Equal to the filename of your component.

import datetime
import logging

from homeassistant.helpers.entity import Entity
from liberation_direct import LiberationDirect

DOMAIN = "liberation_recap"
_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the LiberationRecap component."""
    
    entity = LiberationRecap()
    add_entities([entity], True)
    
    return True
    

class LiberationRecap(Entity):
    """ Retrieves the latest news summary and converts it to markdown. """

    def __init__(self):
        
        super().__init__()
        self._api = LiberationDirect()
        self._name = "Libération - Dernier récap"
        self._state = datetime.datetime.now()
        self._unit_of_measurement = None
        self._attributes = {}
    
    @property
    def name(self):
        return self._name
        
    @property
    def state(self):
        return self._state
    
    @property
    def unique_id(self):
        return "sensor.liberation_dernier_recap"
        
    @property
    def state_attributes(self):
        return self._attributes
        
    def update(self):
        
        self._state = datetime.datetime.now()
        self._attributes["recap"] = LiberationDirect().get_news_summary_markdown()

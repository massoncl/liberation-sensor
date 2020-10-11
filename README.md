# liberation-sensor

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This is a custom component for Home Assistant. 
The French newspaper Libération has a [live feed](http://www.liberation.fr/direct) where they regularly post short summaries of current events.
This sensor parses that feed, finds the latest summary and converts it into markdown to be shown in a Markdown card.


This sensor is activated by adding the following into your `configuration.yaml` :

```yaml
sensor:
  - platform: liberation_sensor
    unique_id: "liberation_recap"
    scan_interval: 900
``` 

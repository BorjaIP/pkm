---
title:  Elasticsearch
created: Sunday 30th April 2023 20:43
aliases: elastic
tags: db
---

- [Create a dashboard to visualize application logs in Kibana](https://dev.to/moesmp/create-a-dashboard-to-visualize-application-logs-in-kibana-2h5h)
- [elastic-scripts](https://github.com/BktechBrazil/elastic-scripts/tree/master/es)

## Options

Edit `/usr/share/elasticsearch/config/elasticsearch.yml`.

```yaml
cluster.name: "simple"
network.host: 0.0.0.0
xpack.security.enabled: true
discovery.type: single-node
```

```bash
# auto password
./bin/elasticsearch-setup-passwords auto
# setup custom pass
./bin/elasticsearch-setup-passwords interactive
```

## API

`pip install elasticsearch`

```python
from elasticsearch import Elasticsearch
client = Elasticsearch(hosts="http://username:password@es-endpoint:es-port/")
client.info()
```
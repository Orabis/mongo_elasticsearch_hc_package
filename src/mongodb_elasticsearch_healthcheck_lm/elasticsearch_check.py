import logging
from uuid import uuid4

from django.conf import settings
from elasticsearch import Elasticsearch, ElasticsearchException, RequestError
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException, ServiceReturnedUnexpectedResult


class ElasticSearchCheckBackend(BaseHealthCheckBackend):
    def __init__(self):
        super().__init__()
        self.hc_index = "health_check_test_index"
        self.doc_index = str(uuid4())
        self.es = Elasticsearch(settings.ELASTICSEARCH_DSL["default"]["hosts"])

    def check_status(self):
        logger = logging.getLogger(__name__)
        try:
            self._create_index()
            self._insert_doc()
            self._retrieve_doc()
            self._delete_doc()
        except ElasticsearchException:
            logger.exception("Error in ElasticSearchCheckBackend")
            raise ServiceReturnedUnexpectedResult("Elasticsearch exception")
        except Exception as e:
            logger.exception("Error in ElasticSearchCheckBackend")
            raise HealthCheckException("Unknown exception") from e

    def identifier(self):
        return self.__class__.__name__

    def _create_index(self):
        try:
            self.es.indices.create(
                index=self.hc_index,
                body={
                    "settings": {
                        "number_of_shards": 1,
                        "number_of_replicas": 0,
                    },
                },
            )
        except RequestError:
            # Index already exists
            pass

    def _insert_doc(self):
        doc = {"id": str(uuid4()), "name": "Health Check test"}
        self.es.index(index=self.hc_index, body=doc, id=self.doc_index)

    def _retrieve_doc(self):
        self.es.get(index=self.hc_index, id=self.doc_index)

    def _delete_doc(self):
        self.es.delete(index=self.hc_index, id=self.doc_index)

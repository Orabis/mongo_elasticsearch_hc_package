import logging
from uuid import uuid4

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

from pount.mongo import mongo_db


class MongoDbCheckBackend(BaseHealthCheckBackend):
    def __init__(self):
        super().__init__()
        self.document_id = str(uuid4())
        self.doc = {"_id": self.document_id, "name": "Health Check test"}

    def check_status(self):
        logger = logging.getLogger(__name__)
        try:
            self._insert_doc()
            self._retrieve_doc()
            self._delete_doc()

        except ServerSelectionTimeoutError:
            logger.exception("Backend server timed out")
            raise HealthCheckException("Timed out")
        except PyMongoError:
            logger.exception("Error in MongoDbCheckBackend")
            raise HealthCheckException("MongoDbBackend exception")
        except Exception as e:
            logger.exception("Error in MongoDbCheckBackend")
            raise HealthCheckException("Unknown exception") from e

    def identifier(self):
        return self.__class__.__name__

    def _insert_doc(self):
        mongo_db().healthcheck_collection.insert_one(self.doc)

    def _retrieve_doc(self):
        mongo_db().healthcheck_collection.find_one(self.doc)

    def _delete_doc(self):
        mongo_db().healthcheck_collection.delete_one(self.doc)

"""
Salesforce Data Cloud data loader for Llama Index.

Data is loaded via Data Cloud's Query Svc api
"""

import logging
from typing import List, Optional
from dotenv import load_dotenv
from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document

logger = logging.getLogger(__name__)

load_dotenv()


class DataCloudDataLoader(BaseReader):
    """
    Loads data via a Data Cloud SQL query against the embedding bundle
    """
    def __init__(self, db_path: str, chunk_table: str, vector_table: str, text_column: str,
                 where_clause: Optional[str] = None) :
        super().__init__()
        self.db_path = db_path
        self.chunk_dlm = chunk_table
        self.vector_index_dlm = vector_table
        self.text_column = text_column
        self.where_clause = where_clause

    def load_data(self, **kwargs) -> List[Document]:
        sql = f"""
        SELECT
            index.RecordId__c,
            index.score__c,
            chunk.Chunk__c
        FROM
            vector_search(TABLE({self.vector_index_dlm}), '{self.text_column}', '', 1) AS index
        JOIN
            {self.chunk_dlm} AS chunk
        ON
            index.RecordId__c = chunk.RecordId__c        
        """
        request_obj = {
            "sql": sql
        }
        logger.debug(request_obj)
        response = self.query_svc_client.read_data(request_obj)
        documents = []
        for item in response:
            if item.payload is not 'null':
                documents.append(Document(
                    text=item.payload,
                    metadata={
                        "row_id":item.id,
                        "score":item.score
                    }
                ))
        return documents

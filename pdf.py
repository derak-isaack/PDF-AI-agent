from llama_index.core import SimpleDirectoryReader
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.core.indices.loading import load_index_from_storage

reader = SimpleDirectoryReader(input_files=['./data/ESG-spreads.pdf'])
documents = reader.load_data()

def get_index(data, index_name):
    # storage_context = StorageContext.from_defaults(persist_dir="./data/indexes")
    index = VectorStoreIndex.from_documents(data, show_progress=True)
    index.storage_context.persist(persist_dir=index_name)
    return index



pdf_index = get_index(documents, "pdf_index")
pdf_engine = pdf_index.as_query_engine()
pdf_engine.query("What is the ESG spread?")

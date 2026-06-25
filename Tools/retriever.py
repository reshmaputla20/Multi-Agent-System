class SimpleRetriever:
    def __init__(self, documents: str):
        self.documents = documents

    def get_context(self, query : str) -> str :
        query = query.lower()
        sentences = self.documents.split(".")

        relevant = [s.strip() for s in sentences if any(word in s.lower() for word in query.split())]

        return ". ".join(relevant)
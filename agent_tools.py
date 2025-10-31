from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama


# Initialize the Ollama LLM
llm = Ollama(model="llama3:instruct", temperature=0.7)


def summarize_text(retriever, topic):
    """Generate a study-friendly summary of the given topic."""
    template = PromptTemplate(
        input_variables=["context"],
        template="Summarize the following text for study guides:\n{context}"
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": template}
    )
    return qa_chain.run(topic)


def create_qa_pairs(retriever, topic):
    """Generate educational Q&A pairs."""
    template = PromptTemplate(
        input_variables=["context"],
        template="Generate 5 educational Q&A pairs from this text:\n{context}"
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": template}
    )
    return qa_chain.run(topic)


def create_flashcards(retriever, topic):
    """Generate flashcards with term-definition format."""
    template = PromptTemplate(
        input_variables=["context"],
        template="Create concise flashcards (Term -> Definition) from this content:\n{context}"
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": template}
    )
    return qa_chain.run(topic)

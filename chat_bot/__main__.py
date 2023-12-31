import uvicorn
from fastapi import FastAPI

from chat_bot.config import Config
from chat_bot.logger import logger
from chat_bot.question_answering import QAModel

config = Config()
app = FastAPI()
qa_model = QAModel(
    llm_model_id=config.question_answering_model_id,
    embedding_model_id=config.embedding_model_id,
    index_repo_id=config.index_repo_id,
    api_token=config.huggingface_token,
    use_docs_for_context=config.use_docs_for_context,
    add_sources_to_response=config.add_sources_to_response,
    use_messages_for_context=config.use_messages_in_context,
    num_relevant_docs=config.num_relevant_docs,
    debug=config.debug,
)


@app.get("/chat")
def get_answer(question: str, messages_context: str = ""):
    logger.info(
        f"Received request with question: {question}" f"and context: {messages_context}"
    )
    response = qa_model.get_answer(question=question, messages_context=messages_context)
    return {"answer": response.get_answer(), "sources": response.get_sources_as_text()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(config.port))

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from app.vector_store.vector_store import get_vector_store
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from  .template import * 


class ChatService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-001",
            temperature=0.3,
            google_api_key="AIzaSyDtNR7vQFPaT_YQhfz_EItbwTW4AUBkz6w",
            convert_system_message_to_human=True
        )
        self.vector_store = get_vector_store()
        
        template = template_1
        
        self.qa_prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"],
            partial_variables={"company_name": "Bakr"}
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(),
            chain_type_kwargs={"prompt": self.qa_prompt},
        )

    async def handle_query(self, question: str, chat_history: list):
        response = await self.qa_chain.acall({"query": question})
        return response["result"]
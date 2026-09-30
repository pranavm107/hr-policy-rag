"""Step 5: wrap the retriever as a tool the agent can all."""

from langchain.tools import tool # used to make a tool for agent it convert our function into a tool or llm

def create_search_tool(retriever):
    """Return a @tool function that searches the HR Policy document."""

    @tool
    def search_hr_policy(question: str) -> str:
        """Search the HR policy document for information abou leave, working from home,
        probation, notice_period, reimbursemet, code of conduct, holidays, performance or exit process"""

        matching_chunks = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy
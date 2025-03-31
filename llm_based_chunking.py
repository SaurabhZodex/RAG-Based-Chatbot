# # LLM Proposition splitting with metadata retention
# def split_propositions(document, groq_api_key):
#     llm = ChatGroq(
#         temperature=0.2,
#         model_name="deepseek-r1-distill-llama-70b",
#         groq_api_key=groq_api_key
#     )
    
#     prompt = ChatPromptTemplate.from_template("""
#     Decompose the "Content" into clear, simple propositions following these rules:
#     1. Split compound sentence into simple sentences. Maintain the original phrasing from the input whenever possible.
#     2. For any named entity that is accompanied by additional descriptive information, separate this \
#     information into its own distinct proposition.
#     3. Decontextualize the proposition by adding necessary modifier to nouns or entire sentences \
#     and replacing pronouns (e.g., "it", "he", "she", "they", "this", "that") with the full name of the \
#     entities they refer to.
#     4. Format the output as a JSON list of strings.
    
#     Examples:

#     Content: "The earliest evidence for the Easter Hare was recorded in 1678 by Georg Franck von Franckenau, a \
#             professor of medicine. He went to the park. He likes walking."
#     Output: ["The earliest evidence for the Easter Hare was recorded in 1678 by Georg Franck von Franckenau.", \
#             "Georg Franck von Franckenau was a professor of medicine.", 'Georg Franck went to the park.', 'Georg Franck likes walking']
    
#     ### Content: 
#     {text}
#     """)
    
#     # chain = LLMChain(llm=llm, prompt=prompt)
#     # result = chain.invoke({"text": document.page_content})
#     # use it in a runnable
#     runnable = prompt | llm
#     result = runnable.invoke({
#             "text": document.page_content
#         }).content
#     # print(result)
#     try:
#         # Extract the LLM's response after the <think> tag
#         answer_content = result['text'].split('</think>')[1].strip()
#         # print(answer_content)
#         props = eval(answer_content)
#         # Create new documents with original metadata
#         return [
#             Document(
#                 page_content=prop,
#                 metadata={
#                     **document.metadata,
#                     "original_start_index": document.metadata.get("start_index", 0),
#                     "proposition_index": i
#                 }
#             ) for i, prop in enumerate(props)
#         ]
#     except Exception as e:
#         # Fallback: return original document
#         return [document]

# # Load the API key from .env file
# load_dotenv()
# chatgroq_api_key = os.getenv("GROQ_API_KEY")

# # Process all chunks through LLM
# proposition_chunks = []
# for chunk in primary_chunks[:10]:
#     proposition_chunks.extend(split_propositions(chunk, chatgroq_api_key))
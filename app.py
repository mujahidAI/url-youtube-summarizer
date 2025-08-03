import streamlit as st 
import validators
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from pytubefix import YouTube


st.set_page_config(page_title="youtube / website content summarizer",page_icon="🦜")
st.title("🦜 Langchain: Summarize Text from yt or website")
st.subheader("summerize URL")

with st.sidebar:
    groq_api_key=st.text_input("Groq Api Key",value="",type="password")

url=st.text_input("URL",label_visibility="collapsed")
# llm=ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)

prompt=""" 
You are an expert summarizer.

Summarize the following content clearly and concisely in **no more than 300 words**. Focus on the **main points, key insights, and important takeaways**, while preserving the original meaning and tone.
enlist main points 
Avoid repeating examples or minor details. Write in professional yet accessible language 

content:{text}
"""
prompt=PromptTemplate(template=prompt,input_variables=["text"])


if st.button("Summarize the content from Yt or Web"):
    if not groq_api_key.strip() or not url.strip():
        st.error (" plaese provide the required information")

    elif not validators.url(url):
        st.error("please enter a valid url ( yt or website)")
    
    else:
        try:
            with st.spinner("waiting..."):
                # llm=ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)
                llm=ChatGroq(model="llama3-8b-8192",groq_api_key=groq_api_key)
    
                if "youtube.com" in url:
                    loader=YoutubeLoader.from_youtube_url(url,add_video_info=True)
    
                else:
                    loader=UnstructuredURLLoader(urls=[url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                # Step 1: Split the documents into smaller chunks
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,  # You can adjust this
                    chunk_overlap=200
                )
                split_docs = splitter.split_documents(docs)

                # Step 2: Use a map-reduce summarization chain
                chain = load_summarize_chain(
                    llm,
                    chain_type="map_reduce",  # Handles long texts
                    map_prompt=prompt,
                    combine_prompt=prompt
                )

                # Step 3: Run the chain
                output_summary = chain.run(split_docs)





               
               
               
               
               
               
               
               
                # chain=load_summarize_chain(
                #     llm,
                #     chain_type="stuff",
                #     prompt=prompt
                # )





                output_summary=chain.run(docs)
                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")
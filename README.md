<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">LangChain LLM arXiv tool </h3>

  <p align="center">
    PoC of reading arXiv papers using LLMs
    <br />
  </p>
</div>


Original idea from Rappy Saha over lunch.
Initial implementation Perry Gibson.
PRs welcome

The purpose of this codebase to demonstrate using the LangChain tool + some LLM to provide intelligent search over arXiv papers.

To run this basic implementation, first you need [an OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).

You then set it as an environment variable:

``` sh
export OPENAI_API_KEY=sk-example_key
```

Then, make sure you have installed the python packages.

``` sh
pip3 install -r requirements.txt
```


Now, right now the code has two scripts.

- `fetch_papers.py` - gets the raw LaTeX of recent arXiv papers and copies them into `papers_db`.
- `llm_query.py` - reads the papers along with questions and tries to answer them.


Things that need to be improved:
- the search, download, and copy process is quite basic.  It only searches for random machine learning papers, and does not filter them in anyway.
- It could be interesting to get all the machine learning papers for each day and do a summary.
- the LaTeX file copier does not currently account for the source being across several files.  [This code from my thesis-o-meter](https://github.com/Wheest/thesis-o-meter/blob/main/tex_file_processor.py) could help deal with this case
- The questions being asked are not very deep
- There is not a way right now to select the LLM that is being used
- It would be good if we could save the semantic embeddings of the papers to disk, which would reduce inference time
- Right now it only reads LaTeX but many papers are just PDF.  Should use pandoc or something to cover the PDF case

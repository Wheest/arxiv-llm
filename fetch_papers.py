#!/usr/bin/env python3

import os
import arxiv
import feedparser
import time
import urllib.request
import shutil


def download_file_with_progressbar(url, destination):
    with urllib.request.urlopen(url) as response, open(destination, "wb") as out_file:
        shutil.copyfileobj(response, out_file)


# Set the path where you want to save the files
path = "papers/"

# Query for the 10 most recent papers
root_url = "http://export.arxiv.org/api/query?"
search_query = "all:machine+learning"  # change this to your needed category of research
start_index = 0
results_per_iteration = 20

# Download the 10 most recent papers
query = f"{root_url}search_query={search_query}&start={start_index}&max_results={results_per_iteration}"
feed = feedparser.parse(query)

for entry in feed.entries:
    paper_id = entry.id.split("/")[-1]

    print(paper_id)
    if "." not in paper_id:
        continue
    # print(f"Downloading {paper_id}...")
    # try:
    #     paper = next(arxiv.Search(id_list=[paper_id]).results())
    #     paper.download_source(entry, dirpath=path)
    #     print(f"Successfully downloaded {paper_id}")
    # except Exception as e:
    #     print(f"Failed to download {paper_id}: ", e)

    src_url = entry.link.replace("/abs/", "/src/")
    dst_file = os.path.join(path, paper_id + ".tar.gz")
    try:
        download_file_with_progressbar(src_url, dst_file)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Source files not found for {}".format(paper_id))
        else:
            raise
    time.sleep(
        10
    )  # respect arXiv's "no more than one request every three seconds" rule


import os
import tarfile
import glob
import shutil

source_directory = path
destination_directory = "papers_db/"

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

for tar_file in glob.glob(os.path.join(source_directory, "*.tar.gz")):
    paper_id = os.path.basename(tar_file).split(".tar.gz")[0]
    with tarfile.open(tar_file) as archive:
        for file in archive.getnames():
            if file.endswith(".tex"):
                print(file, source_directory)
                source = archive.extract(file, path=source_directory)
                destination = os.path.join(destination_directory, f"{paper_id}.tex")
                print(source)
                shutil.move(os.path.join(source_directory, file), destination)

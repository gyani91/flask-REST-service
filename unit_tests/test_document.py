from api.document import store_document, retrieve_document, retrieve_summary, delete_document


def test_store_document_retrieve_document_summary():
    url = "http://localhost:5000"
    document = "Computer Science graduate with 4.5 years of industry experience. I am currently working with Nomoko as a Machine Learning Engineer. I have done my Masters in Artificial Intelligence at USI and ETH Zürich, where I have completed coursework in Machine Learning, Deep Learning, Computer Vision, High-Performance Computing, Robotics, and Quantum Computing taught by the members of Dalle Molle Institute for Artificial Intelligence Research (IDSIA). I undertook my Master Thesis at the Mixed Reality and AI Lab at Microsoft Research, Zürich under the supervision of Prof. Marc Pollefeys."
    summary = "I have done my Masters in Artificial Intelligence at USI and ETH Zürich, where I have completed coursework in Machine Learning, Deep Learning, Computer Vision, High-Performance Computing, Robotics, and Quantum Computing taught by the members of Dalle Molle Institute for Artificial Intelligence Research (IDSIA)"

    # Store the document
    document_id = store_document(url, document)

    # Retrieve the document
    retrieved_document = retrieve_document(url, document_id)

    assert retrieved_document["text"] == document

    # Retrieve the summary
    retrieved_summary = retrieve_summary(url, document_id)

    # This assert might break if summarization technique is changed
    assert retrieved_summary["summary"] == summary

    # Delete this entry
    delete_document(url, document_id)

    assert retrieve_document(url, document_id) == "Not Found"


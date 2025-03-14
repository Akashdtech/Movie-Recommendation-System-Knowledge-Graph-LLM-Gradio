# Movie-Recommendation-System-Knowledge-Graph-LLM-AI-Agents-Gradio
This project constructs a knowledge graph from the TMDB 5000 Movies dataset and utilizes a custom LLM-based approach to recommend similar movies based on shared attributes such as genre, cast, crew, and keywords.

Data Loading and Preprocessing:

    Loads movie metadata and credits from CSV files.
    Merges datasets on the movie title.

Knowledge Graph Construction:

    Uses rdflib to create an RDF-based knowledge graph.
    Stores movie attributes as RDF triples.
    Converts the RDF graph to a NetworkX graph for further processing.
    Exports the graph data to a CSV file (knowledge_graph.csv).

Custom LLM Integration:

    Implements a custom LLM class using the Hugging Face API.
    Constructs prompts dynamically to query the LLM for movie recommendations.

Movie Recommendation System:

    Uses the knowledge graph and LLM to suggest movies similar to a given title.

Dependencies:

    !pip install langchain
    !pip install langchain_community
    !pip install networkx
    !pip install rdflib

Usage:

    Prepare the dataset: Ensure the TMDB 5000 Movies dataset files (tmdb_5000_movies.csv and tmdb_5000_credits.csv) are available.
    Run the script: Execute the Python code to construct the knowledge graph and initialize the LLM.
    Get Movie Recommendations: Call get_similar_movies("Movie Title") to receive a list of similar movies.

Example:

    movie_title = "The Avengers"
    similar_movies = get_similar_movies(movie_title)
    print(similar_movies)

API Integration:

    The script uses Hugging Face's Meta-Llama-3-8B-Instruct model for movie recommendations.
    The API key must be set in the headers dictionary for authorization.

Output:

    A CSV file (knowledge_graph.csv) containing the extracted triples.
    A list of recommended movies based on the provided movie title.

Future Improvements:

    Enhance similarity scoring using graph-based algorithms.
    Expand the knowledge graph with additional relationships.
    Integrate more advanced LLMs for improved recommendations.

This project leverages AI-driven knowledge graph techniques and LLM-based reasoning to provide intelligent movie recommendations.


import gradio as gr
from movie_recommendation_system import get_similar_movies # The movie-recommendation-system.ipynb file should be converted to .py file for this import to work

interface = gr.Interface(fn=get_similar_movies,
                        inputs=gr.Textbox(lines=2, placeholder="Enter a movie title"),
                        outputs="text",
                        title="Movie Recommendation System",
                        description="Enter a movie title to get similar movies.")

interface.launch()

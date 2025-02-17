import gradio as gr
from recommendation import get_similar_movies # Import from recommendation.py file

interface = gr.Interface(fn=get_similar_movies,
                        inputs=gr.Textbox(lines=2, placeholder="Enter a movie title"),
                        outputs="text",
                        title="Movie Recommendation System",
                        description="Enter a movie title to get similar movies.")

interface.launch()

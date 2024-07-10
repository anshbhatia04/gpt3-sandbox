import os
import sys

from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = "answers: "
answer_prefix = "clue: "

# Construct GPT object and show some examples
gpt = GPT(engine="davinci", 
temperature=0.7, 
max_tokens=6,
input_prefix=question_prefix,
output_prefix=answer_prefix,
append_output_prefix_to_query=False)

gpt.add_example(Example("answers: nut, bark", "clue: tree"))
gpt.add_example(Example("answers: trick, spells, wizard, enchanted, mystic", "clue: magic"))
gpt.add_example(Example("answers: football, soccer, rugby, tennis", "clue: sport"))
gpt.add_example(Example("answers: yarn, shoe, knit, stocking", "clue: sock"))

# Define UI configuration
config = UIConfig(
    description="Use GPT3 to Dominate Codenames",
    button_text="Generate Clue",
    placeholder="Add your spymaster words separated by commas",
    show_example_form=False,
)

demo_web_app(gpt, config)
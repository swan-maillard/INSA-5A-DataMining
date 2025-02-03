# Test
import time
curr_date = time.strftime("%Y-%m-%d")

planner_prompt = """
Current time: {curr_date}

For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Objective: {objective}
"""

# planner.invoke([SystemMessage(content=planner_prompt.format(curr_date=curr_date, objective="what is the hometown of the current Australia open winner"))])
# Test

replanner_prompt = """
Current time: {curr_date}

For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Your objective was this:
{input}

Your original plan was this:
{plan}

You have currently done the follow steps:
{past_steps}

Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.
"""

# replanner.invoke(
#     [
#         SystemMessage(
#             content=replanner_prompt.format(
#                 curr_date=curr_date,
#                 input="what is the hometown of the current Australia open winner",
#                 plan=[
#                     "Identify the current year of the Australia Open winner.",
#                     "Search for the winner of the Australia Open in that year.",
#                 ],
#                 past_steps=["Identify the current year of the Australia Open winner"],
#                 response="",
#             )
#         )
#     ]
# )

# Test
code_gen_prompt = """You are a machine Learning coding assistant in python.
Answer the user question. Ensure any code you provide can be executed with all required imports and variables defined. 
Structure your answer with a description of the code solution.
Then list the imports. And finally list the functioning code block. Here is the user question and feedback:
{messages}
"""

# code_gen_llm.invoke(
#     ("user", code_gen_prompt.format(messages="How can I load a CSV file in pandas?"))
# )
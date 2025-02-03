base_prompt = """You are a Data Science and Machine Learning expert.

I'm working on a data science problem that I divided into the following phases:
- problem understanding
- data exploration and preprocessing
- feature engineering
- model building
- answer submission

Here's the context of the problem:
{context}

I'm currently at the phase {phase}, here's what I've done so far:
{summary}
"""

reader_prompt = """You are a Data Science and Machine Learning expert. 
You are tasked with tasked with understanding a machine learning problem given a problem statement overview and a dataset description.

Here's the problem statement overview:

{problem_statement}

Here's the dataset description:

{dataset_description}

Examine the optional feedback given below:

{feedback}


Explain in great details the following:
- The problem statement
- The files needed to solve the problem
- The path to those files. This is VERY important. Don't skip this step.
- What is the data format, a clear description of the columns and their meaning
- What is the prediction target and how it should be submitted
- What acronyms are used in the problem statement

Be exhaustive in your explanation. Format your response in markdown.
"""

planner_prompt = (
    base_prompt
    + """For the given phase {phase}, come up with a simple step by step plan. A developer will follow this plan and implement the steps in python.
This plan should involve individual tasks, that if executed correctly will yield useful results. Do not add any superfluous steps. 
Make sure that each step has all the information needed - do not skip steps

Here is some information about what to do for the current phase:
{information}

Here are some general guidelines for the plan:
- do not generate plots or visualizations in this phase. Prefer textual summaries.
- generate no more than 5 steps
"""
)


replanner_prompt = (
    base_prompt
    + """For the given phase {phase}, come up with a simple step by step plan. A developer will follow this plan and implement the steps in python.
This plan should involve individual tasks, that if executed correctly will yield useful results. Do not add any superfluous steps. 
Make sure that each step has all the information needed - do not skip steps

Here is some information about what to do for the current phase. You can take inspiration from this:
{information}

Here was your original plan:
{plan}

Here are the steps you have already done:
{past_steps}

Update your plan accordingly. If no more steps are needed you can fill the response with END. Otherwise, fill out the plan.
Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.

"""
)


summarizer_prompt = (
    base_prompt
    + """To solve this phase you taken the following steps:
{steps}

Now summarize the key insights and findings from those steps, including but not limited to:
- description of the final dataset: columns, data types, etc.
- key observations from data exploration
- any preprocessing steps taken
- initial insights for feature engineering
- the output files generated
- the python code file generated

"""
)


developer_prompt = (
    base_prompt
    + """You are a Data Science and Machine Learning expert.
You are are tasked with coding a solution in python following the planner provided plan : 
{plan}

Implement step 1 of the plan: {step}

You may use public libraries and packages: pandas, numpy, scikit-learn.
"""
)

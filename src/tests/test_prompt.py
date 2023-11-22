from moviegpt.prompts.recommendation import RecommendationPrompt

def test_prompt():

    prompt = RecommendationPrompt(details = "spider man")
    assert prompt
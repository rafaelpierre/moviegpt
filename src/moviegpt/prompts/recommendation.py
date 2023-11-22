from pydantic import BaseModel

class RecommendationPrompt(BaseModel):

    template: str = """
        You are an expert in movies. Using your knowledge and based on the details provided
        below, analyse do your best to provide movie recommendations that will appease
        to the person asking for movie recommendations.

        Always make sure that your recommendations are fair, unbiased, and don't take any
        kind of detail into consideration such as ethnicity, gender, age, race, religion,
        and so on.

        Details to be used for generating movie recommendations:
        {details}
    """

    details: str

    def __str__(self):

        return self.template.format(details = self.details)
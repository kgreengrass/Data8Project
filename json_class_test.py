from json_class import ReadTransformJson
import pandas as pd
import pytest


def test_ReadTransformJson():
    test_instance = ReadTransformJson('data8-engineering-project', 'json_class_testing')
    interview_notes_df = test_instance.json_reader()
    d_test = {"name": "Manon Clutterham", "date": "11/9/2019",
              "strengths": ["Patient", "Listening", "Innovative"],
              "weaknesses": ["Sensitive", "Passive", "Introverted"],
              "technologies": [{"language": "Python", "self_score": 4},{"language": "Java", "self_score": 5},
                               {"language": "SPSS", "self_score": 4}], "self_development": "Yes", "geo_flex": "Yes",
              "financial_support_self": "Yes", "result": "Pass", "course_interest": "Business"}
    test_df = pd.json_normalize(d_test)
    assert interview_notes_df.equals(test_df)




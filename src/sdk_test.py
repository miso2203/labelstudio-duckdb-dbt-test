import os
import json
from label_studio_sdk import Client
from label_studio_sdk.label_interface import LabelInterface
from label_studio_sdk.label_interface.create import labels

LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = os.getenv("LABELSTUDIO_API_KEY")

ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)

project = ls.start_project(
    title='SDK_TEST_2',
    description="Project description test",
    label_config=LabelInterface.create({
      "image": "Image",
      "bbox": labels(["brand", "size", "dot"], tag_type="RectangleLabels")
    })
)

json_file_path = '/Users/bella.s./Documents/labelstudio-duckdb-dbt-test/data/pre_annotation_json/test.json'

with open(json_file_path, 'r') as file:
    tasks = json.load(file)

response = project.import_tasks(tasks)

print(f"업로드된 작업 수: {len(response)}")
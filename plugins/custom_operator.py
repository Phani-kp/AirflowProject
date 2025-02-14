from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super(CustomOperator, self).__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        self.log.info(f"Executing custom operator with param: {self.param}")

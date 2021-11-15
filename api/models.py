from django.db import models


class RefData(models.Model):
    # Reference (or ID). Corresponds to source dataset filename without extension
    ref = models.CharField(max_length=128)

    # DEPRECATED: Use ref
    ref_id = models.CharField(max_length=64)

    # DEPRECATED: Use ref
    ref_type = models.CharField(max_length=24)

    # Matches ID in settings.RELATON_DATASETS
    dataset = models.CharField(max_length=24)

    body = models.JSONField('body')

    class Meta:
        db_table = 'api_ref_data'

        constraints = [
            models.UniqueConstraint(fields=['ref_id', 'dataset'], name='unique_dataset_id')
        ]

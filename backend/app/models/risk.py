#风险评估相关模型
from tortoise import fields, models

class RiskCategory(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)

    class Meta:
        table = "risk_category"

class RiskSubcategory(models.Model):
    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField("models.RiskCategory", related_name="subcategories")
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)

    class Meta:
        table = "risk_subcategory"

class RiskAssessment(models.Model):
    id = fields.IntField(pk=True)
    company = fields.ForeignKeyField("models.Company", related_name="assessments")
    overall_risk_level = fields.CharField(max_length=50)
    assessment_date = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "risk_assessment"

class CheckResult(models.Model):
    id = fields.IntField(pk=True)
    assessment = fields.ForeignKeyField("models.RiskAssessment", related_name="check_results")
    subcategory = fields.ForeignKeyField("models.RiskSubcategory", related_name="check_results")
    result = fields.TextField()
    risk_level = fields.CharField(max_length=50)
    checked_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "check_result"
